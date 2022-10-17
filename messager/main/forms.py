from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError


class LoginForm (FlaskForm):
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Log In')


class CreateUser (FlaskForm):
    first_name = StringField('First Name', validators=[data_required()]) 
    last_name = StringField('Last Name', validators=[data_required()])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Create')
