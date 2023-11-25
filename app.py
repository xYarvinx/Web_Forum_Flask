# app.py
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'forum.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from Model.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from Controller import forum, auth  # Import after db is defined to avoid circular imports

app.register_blueprint(forum.forum)
app.register_blueprint(auth.auth)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

# flask shell
# >>> from app import db
# >>> db.create_all()
