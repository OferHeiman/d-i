from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import InputRequired, Email, ValidationError
from passlib.hash import pbkdf2_sha256
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class UsersForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4, max=25, message='Username must be between 8-64 characters'),
                                        validators.InputRequired("Username Required")])
    email = StringField("Email",
                        validators=[InputRequired("Email Required"), Email(message='Please input a valid email')])
    password = PasswordField("Password", [validators.InputRequired("Password Required"),
                                          validators.EqualTo('confirmpassword', message="Passwords must match"),
                                          validators.Length(min=8, max=64, message='Password must be between 8-64 characters')])
    confirmpassword = PasswordField('Confirm Password')
    submit = SubmitField("Submit")

    @staticmethod
    def validate_username(self, username):
        user_object = Users.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists")

    @staticmethod
    def validate_email(self, email):
        user_object = Users.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already exists")

    def __repr__(self):
        return '<Name %r>' % self.name


def invalid_credentials(form, field):
    username_entered = form.username.data
    password_entered = field.data
    user_object = Users.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or password is incorrect")


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(message="Username required")])
    password = PasswordField('Password',
                           validators=[InputRequired(message="Password required"),
                                       invalid_credentials])
    submit = SubmitField("Login")





# delete from users where X
