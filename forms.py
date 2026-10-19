from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Full Name",
        validators=[
            DataRequired(message="Please enter your full name."),
            Length(min=2, max=100, message="Name must be between 2 and 100 characters.")
        ]
    )
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(message="Please enter your email address."),
            Email(message="Please enter a valid email address.")
        ]
    )
    subject = StringField(
        "Subject",
        validators=[
            DataRequired(message="Please enter a subject."),
            Length(min=3, max=150, message="Subject must be between 3 and 150 characters.")
        ]
    )
    category = SelectField(
        "Category",
        choices=[
            ("General Inquiry", "General Inquiry"),
            ("Feedback & Suggestions", "Feedback & Suggestions"),
            ("Project / Infrastructure Concern", "Project / Infrastructure Concern"),
            ("Security & Public Safety", "Security & Public Safety"),
            ("Media & Press Inquiry", "Media & Press Inquiry")
        ],
        default="General Inquiry"
    )
    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Please enter your message."),
            Length(min=10, max=2000, message="Message must be at least 10 characters long.")
        ]
    )
    submit = SubmitField("Send Message")