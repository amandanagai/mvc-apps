from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
	pet_name = StringField('pet_name', validators=[DataRequired()])
	pet_age = IntegerField('pet_age', validators=[DataRequired()])