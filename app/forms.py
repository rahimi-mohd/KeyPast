from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, IntegerField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    app_name = StringField("Title", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    characters = IntegerField("How many characters", validators=[DataRequired()])
    url = StringField("url")
    generate = SubmitField("Generate")
    remember = BooleanField("Remember")
