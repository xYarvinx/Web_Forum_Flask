from flask import Blueprint, render_template, redirect, url_for
from Model.models import User
from app import db
from forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)







@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(username=form.username.data, email=form.email.data)
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('forum.index'))
    return render_template('register.html', form=form)



@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #######################################################################

        if form.email.data == '123123' and form.password.data == '123123':
            # If user credentials are valid, redirect to the index page
            return redirect(url_for('register.index'))  # Use the endpoint name 'forum.index' instead of the URL path '/forum'
        else:
            # If user credentials are invalid, you can render the login template again with an error message
            return render_template('login.html', form=form, error='Invalid username or password')
    return render_template('login.html', form=form)



@auth.route('/logout')
def logout():
    # Логика выхода пользователя
    return redirect(url_for('index'))  # Use the endpoint name 'index' instead of the URL path '/'
