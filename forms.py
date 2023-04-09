from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, length, Regexp, Email, EqualTo, ValidationError
from chow_app.models import Contact, User

class ContactForm(FlaskForm):
    fullname = StringField("fullname",
        validators=[
            DataRequired(),
            length(min=2, max=30, message = "Please provide a valid name"),
            Regexp(
                "^[A-Za-z]  [A-Za-z.]*", 0, "Your Last name must contain only letters")],
        render_kw={"placeholder": "Full name"})

    mail = StringField("mail",
        validators=
            [DataRequired(),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Email address"})

    phone = StringField("phone",
        validators=[
            DataRequired(),
            length(min=2, max=50, message = "Please provide a valid name")],
        render_kw={"placeholder": "Phone number"})

    message = TextAreaField("message",
        validators=[
            DataRequired(),
            length(min=3, max=1000, message = "Please provide a valid name")],
        render_kw={"placeholder": "Your text here..."})
    
    submit = SubmitField("Send Message")


class LoginForm(FlaskForm):
    email = StringField("email",
        validators=
            [DataRequired(),
            length(min=6, max=30),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Enter your email address"})
    
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=8, max=20)],
            render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")




class SignUpForm(FlaskForm):
    fullname = StringField("fullname",
    validators=[
        DataRequired(),
        length(min=1, max=20, message = "Please provide a valid name"),
        Regexp(
            "^[A-Za-z]x*", 0, "Your First name must contain only letters"
            ),
        ],
    render_kw={"placeholder": "What's your name"})

    phone = StringField("phone",
        validators=[
            DataRequired(),
            length(min=1, max=20, message = "Please provide a valid phone number"),
            Regexp(
                "^[A-Za-z] [A-Za-a0-9.]*", 0, "Please provide a valid phone number")],
        render_kw={"placeholder": "Enter your phone number"})

    email = StringField("email",
        validators=
            [DataRequired(),
            length(min=6, max=30),
            Email()],
            render_kw={"placeholder": "Enter your email address"})

    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=6, max=20)],
            render_kw={"placeholder": "Enter your password"})

    confirm_password = PasswordField("confirm_password",
        validators=
            [DataRequired(),
            length(min=6, max=20)],
            render_kw={"placeholder": "Confirm your password"})
    EqualTo("password", message = "The passwords must match! ")
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        user = User.query.filter_by(user_email = email.data).first()
        if user:
            raise ValidationError("That email already has an account. Please choose a different one.")
