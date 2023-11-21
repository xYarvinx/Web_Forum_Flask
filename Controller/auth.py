from flask import Blueprint, render_template, redirect, url_for
from Model.models import User
from app import db
from forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Logic to create a new user based on the form data
        user = User(username=form.username.data, email=form.email.data)
        user.password = form.password.data
        # Add the new user to the database session
        db.session.add(user)
        db.session.commit()
        # Redirect to the index page after successful registration
        return redirect(url_for('forum.index'))  # Use the endpoint name 'forum.index' instead of the URL path '/forum'
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Логика обработки формы входа
        return redirect(url_for('forum.index'))  # Use the endpoint name 'forum.index' instead of the URL path '/forum'
    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    # Логика выхода пользователя
    return redirect(url_for('index'))  # Use the endpoint name 'index' instead of the URL path '/'
