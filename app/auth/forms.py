from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, DataRequired, Email, EqualTo

# local imports
from app.models import User


class RegistrationForm(FlaskForm):
    """ Form for users to create new account """

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                   EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use!')


class LoginForm(FlaskForm):
    """ Form for users to login """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
