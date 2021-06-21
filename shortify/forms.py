from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class UrlForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Shortify")