from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, equal_to

class loginform(FlaskForm):
    username = StringField("Enter your username",validators=[DataRequired()] )
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=6, max=14,)])
    submit = SubmitField("Log in")

class registerform(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(),  Length(min=3, max=30,)] )
    password = PasswordField("Enter your password",)
    repeatpassword = PasswordField('Repeat your password',  validators=[DataRequired(), Length(min=6, max=14,)])
    submit = SubmitField("Register")
    

class productform(FlaskForm):
    img = FileField()
    name = StringField("Product name")
    price = IntegerField("price")

    submit = SubmitField("Post Product")