import json
import unittest
from pathlib import Path

from app import app


DATA_DIR = Path(app.root_path) / "data"


class DirectoryRouteTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()

    def load_records(self, filename):
        with (DATA_DIR / filename).open(encoding="utf-8") as file:
            return json.load(file)

    def assert_directory_filters(
        self, route, filename, name_key, ward_key
    ):
        records = self.load_records(filename)
        self.assertTrue(records, f"{filename} should contain records")

        response = self.client.get(route)
        self.assertEqual(response.status_code, 200)

        page = response.get_data(as_text=True)
        self.assertIn(records[0][name_key], page)

        # Searching for a record's name should return that record.
        search = self.client.get(
            route, query_string={"q": records[0][name_key]}
        )
        self.assertEqual(search.status_code, 200)
        self.assertIn(
            records[0][name_key],
            search.get_data(as_text=True),
        )

        # A search with no matching text must not display known records.
        no_match = self.client.get(
            route,
            query_string={"q": "zz_no_matching_directory_record_93821"},
        )
        self.assertEqual(no_match.status_code, 200)
        no_match_page = no_match.get_data(as_text=True)

        for record in records:
            self.assertNotIn(record[name_key], no_match_page)

        # A ward filter must exclude records belonging to other wards.
        selected_ward = records[0].get(ward_key)
        if selected_ward:
            filtered = self.client.get(
                route, query_string={"ward": selected_ward}
            )
            self.assertEqual(filtered.status_code, 200)
            filtered_page = filtered.get_data(as_text=True)

            for record in records:
                name = record.get(name_key)
                ward = record.get(ward_key)

                # Compare complete rendered headings, not substrings:
                # "Islamiya Primary School" also appears inside
                # "Islamiya Primary School Obagaji".
                rendered_heading = f">{name}</h2>"

                if ward == selected_ward:
                    self.assertIn(rendered_heading, filtered_page)
                elif name:
                    self.assertNotIn(rendered_heading, filtered_page)

    def test_schools_directory_and_filters(self):
        self.assert_directory_filters(
            "/schools", "schools.json", "name", "ward"
        )

    def test_healthcare_directory_and_filters(self):
        self.assert_directory_filters(
            "/health-facilities",
            "health_facilities.json",
            "name_source",
            "ward_source",
        )


if __name__ == "__main__":
    unittest.main()
