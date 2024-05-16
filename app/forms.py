from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class MyForm(FlaskForm):
    app_name = StringField("Title", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    characters = IntegerField("How many characters", validators=[DataRequired()])
    url = StringField("url")
    generate = SubmitField("Generate")
    remember = BooleanField("Remember")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Re-Type password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")
