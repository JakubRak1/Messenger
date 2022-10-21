from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from messenger.models import People


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


    def validate_email(self, email):
        user = People.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in db chose another one')


class CreateMessage(FlaskForm):
    content = TextAreaField ('Content of Message')
    reciver_email = StringField('Reciver Email', validators=[data_required()])
    submit = SubmitField('Send') 


class ReplyMessage(FlaskForm):
    content = TextAreaField ('Content of Message')
    submit = SubmitField('Send') 