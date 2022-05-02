# Form Based Imports
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo, NumberRange
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# User Based Imports
from flask_login import current_user
from mastermindweb.models import User


class GuessingForm(FlaskForm):
    guesscombo = IntegerField('guess',validators=[DataRequired(), NumberRange(max=9999)])
    submit = SubmitField('Guess!')

    def validate_guess(form, field):
        if str(field) == "0000":
            return True
        elif not field or len(str(field.data)) > 4:
            return False




####Use below to check whether current guess already exists in database
####To decide later whether to insert previous guesses to databases or simply use add to a  set and lookup later#

#    def validate_guess(self, guess):
 #       if User.query.filter_by(guess=self.guess.data).first():
  #          raise ValidationError('You have made this guess already')
