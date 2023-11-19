from flask import Flask, render_template, redirect, url_for
from Forum.forms import  RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    title = 'Главное меню'
    return render_template('index.html', title=title)

@app.route('/forum')
def forum():
    forum_name = 'Форум'
    return render_template('forum.html', forum_name=forum_name)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Логика обработки формы регистрации
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Логика обработки формы входа
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    # Логика выхода пользователя
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
