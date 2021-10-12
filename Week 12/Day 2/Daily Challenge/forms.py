from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Name")
    age = TextField('Age')
    phone = TextField('Phone')
    email = TextField("Email")
    experience = TextAreaField("experience")
    education = TextAreaField("education")
    submit = SubmitField("Send")