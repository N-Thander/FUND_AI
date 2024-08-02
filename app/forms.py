from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUp(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# class log in will be in a similar format