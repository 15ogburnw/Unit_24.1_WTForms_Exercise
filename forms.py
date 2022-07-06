from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):

    """Form for adding pets to the adoption app"""

    name = StringField('Animal Name', validators=[InputRequired(
        message='Please provide a name for the animal!')])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[
                          InputRequired(message='Please provide a species!')])
    photo_url = StringField('Photo URL', validators=[
        URL(message=('URL is not valid!')), Optional()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(
        min=0, max=30, message='Age must be between 0-30!')])
    notes = TextAreaField('Notes', validators=[Optional()])


class EditPetForm(FlaskForm):

    """Form for editing existing pets"""

    photo_url = StringField('Photo URL', validators=[
        URL(message=('URL is not valid!')), Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = SelectField('Availability', choices=[(
        'True', 'Available'), ('False', 'Not Available')], validators=[InputRequired()], coerce=lambda x: x == 'True')
