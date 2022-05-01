# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# User Based Imports
from flask_login import current_user
from mastermindweb.models import User


class GuessingForm(FlaskForm):
    guesscombo = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Guess!')



####Use below to check whether current guess already exists in database
####To decide later whether to insert previous guesses to databases or simply use add to a  set and lookup later#

#    def validate_guess(self, guess):
 #       if User.query.filter_by(guess=self.guess.data).first():
  #          raise ValidationError('You have made this guess already')
