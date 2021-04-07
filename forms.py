from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    done = SelectField('done', choices=[('Tak', True), ('Nie', False)], validators=[DataRequired()])
