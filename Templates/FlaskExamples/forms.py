from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

#from models import User



class ExampleDataForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('name')
    text = StringField('text')
    submit = SubmitField('create')

# the validator file means that the data is required

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         if User.query.filter_by(username=username.data).first():
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#        if User.query.filter_by(email=email.data).first():
#             raise ValidationError('Please use a different email address.')