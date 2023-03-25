from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from flask_sqlalchemy import SQLAlchemy

from models import User, db

login_blueprint = Blueprint('login', __name__, template_folder='templates')


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        return "Registered success", User.username
    return render_template('register.html', form=form)


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Length(min=6, max=35)])
    submit = SubmitField('Sign In')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if User.query.filter(User.username == form.username).count() > 0:
        print("USER EXISTS")
        return render_template('index.html', form=form)

    print(form.username)

    return render_template('login.html', form=form)
