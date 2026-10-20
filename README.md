# Agatu Local Government Area Website

A Flask-based website providing information about Agatu Local Government Area (LGA), Benue State, Nigeria. The project brings together local government information, development projects, ward records, administrative directories, and public news in one accessible platform.

## Overview

The Agatu LGA website is designed to make information about the local government and its activities easier to access.

Built with Python and Flask, the website provides public-facing pages for local information and news, alongside administrative functionality for managing news content.

## Features

- **Homepage:** Introduces the local government and highlights selected projects and recent news.
- **About:** Presents information about Agatu LGA and its leadership.
- **Projects:** Displays development projects and available project photographs.
- **News and announcements:** Publishes articles and supporting photographs, including coverage of the SEMA-led flood assessment visit.
- **News administration:** Provides an interface for creating news articles and uploading images.
- **Ward directory:** Lists the ten wards and available polling-unit records.
- **Administration directory:** Presents available information about local government administrations.
- **Departments:** Organises information about local government departments.
- **Contact page:** Provides a public enquiry form interface.
- **Security controls:** Includes environment-based secret-key configuration, CSRF protection, administrative authentication, and image-upload validation.

> **Data accuracy:** Ward, polling-unit, and settlement information should be checked against authoritative sources. Information awaiting confirmation must not be presented as officially verified.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application programming language |
| Flask | Web application framework |
| HTML and CSS | Page structure and styling |
| Bootstrap 5 | Responsive interface |
| Flask-Login | User authentication |
| Flask-WTF | Form handling and CSRF protection |
| Bleach | HTML sanitisation |
| Pillow | Image processing and validation |
| JSON | Storage for selected application data |
| Gunicorn | Production WSGI server |

## Project Structure

```text
agatu_website/
├── app.py
├── data/
│   ├── news.json
│   ├── wards.py
│   └── settlement_research.py
├── static/
│   └── images/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── news.html
│   ├── news_detail.html
│   ├── news_list.html
│   └── admin/
├── tests/
│   └── test_routes.py
├── requirements.txt
├── .gitignore
└── README.md
```

This is a simplified overview. Other templates and files may be present in the repository.

## Requirements

- Python 3.12 or a compatible Python version
- Git
- `pip`
- A terminal on Linux, macOS, or a compatible development environment

## Local Installation

### 1. Get the project

If you already have the repository on your computer, open its directory:

```bash
cd ~/agatu_website
```

If you are setting it up on another computer, clone it using the repository's actual GitHub URL, then enter the cloned directory.

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 4. Configure the secret key

The application requires the `FLASK_SECRET_KEY` environment variable.

For local development, generate a key with:

```bash
export FLASK_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
```

This key remains available in the current terminal session. If you open a new terminal, configure it again.

For production, set a strong, persistent secret through your hosting provider's environment settings. Never commit secret keys or private environment files to Git.

### 5. Run the application

```bash
python3 app.py
```

Open the local address shown in your terminal. By default, Flask commonly uses:

`http://127.0.0.1:5000`

Stop the development server with `Ctrl+C`.

**Important:** Flask's built-in development server is for local development, not production hosting.

## Main Routes

| Route | Purpose |
|---|---|
| `/` | Homepage |
| `/about` | About the local government |
| `/projects` | Development projects |
| `/wards` | Ward directory |
| `/administrations` | Administration records |
| `/departments` | Department information |
| `/contact` | Contact form |
| `/news` | News articles |

Individual news and project pages may be available through their detail routes.

## Testing

Activate the virtual environment and configure `FLASK_SECRET_KEY` before running the tests.

Run the route tests:

```bash
python3 -m unittest discover -s tests -v
```

Check Python syntax:

```bash
python3 -m compileall -q app.py data
```

Validate the news JSON file:

```bash
python3 -m json.tool data/news.json > /dev/null
```

Check unstaged changes for whitespace errors:

```bash
git diff --check
```

To check staged changes instead, run:

```bash
git diff --cached --check
```

## Security and Data Handling

The application includes several security-related measures:

- Secret-key configuration through an environment variable.
- CSRF protection for supported form submissions.
- Authentication for protected administrative functionality.
- Image-upload size and file validation.
- Generated filenames for uploaded images.
- Atomic file replacement when saving news data.

These controls should be tested as the application evolves. In particular, authentication, permissions, upload handling, and error responses should be covered by automated tests.

JSON storage is currently used for selected application data. A database may be appropriate if the application requires more concurrent editing, stronger relational integrity, or expanded operational requirements.

## Known Limitations

- **Contact messages:** The existence of the contact form does not by itself mean messages are delivered or persistently stored. Those behaviours should be verified and implemented where required.
- **Public records:** Ward, polling-unit, settlement, and administration records should be checked against reliable sources and labelled appropriately when verification is incomplete.
- **Automated testing:** The existing route tests should be supplemented with tests for authentication, CSRF protection, news creation, invalid uploads, and error handling.
- **Production readiness:** Deployment configuration, persistent secret management, file permissions, backups, and monitoring must be reviewed for the chosen hosting environment.

## Development Guidelines

When making changes:

1. Inspect the existing implementation before editing.
2. Keep changes focused and preserve working functionality.
3. Run the relevant tests and validation commands.
4. Review the Git diff before committing.
5. Never commit secrets, private user data, or local backup files.
6. Clearly identify public information that has not been officially verified.

## Maintainer

**Antenyi Joseph Ochohepo**

- GitHub: [antenyijoseph20-glitch](https://github.com/antenyijoseph20-glitch)
- Portfolio: [Software development portfolio](https://antenyijoseph20-glitch.github.io/portfolio/)

## Licence

No licence has currently been specified. Until a licence is added to the repository, reuse and redistribution are subject to applicable copyright law.
