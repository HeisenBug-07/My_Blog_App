from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email


class AddPosts(FlaskForm):
    heading = StringField('Heading', validators=[DataRequired(message='provide heading')])
    sub_heading = StringField('Sub heading', validators=[DataRequired(message='provide sub heading')])
    content = TextAreaField('Content', render_kw={"rows":11 , "cols": 70}, validators=[DataRequired(message='provide content')])
    submit = SubmitField('Create Post!')


class EditPosts(FlaskForm):
    heading = StringField('Heading', validators=[DataRequired(message='provide heading')])
    sub_heading = StringField('Sub heading', validators=[DataRequired(message='provide sub heading')])
    content = TextAreaField('Content', render_kw={"rows":11 , "cols": 70}, validators=[DataRequired(message='provide content')])
    submit = SubmitField('Edit Post!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='provide email'), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
