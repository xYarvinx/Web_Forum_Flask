from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'forum.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Controller import forum, auth  # Import after db is defined to avoid circular imports

app.register_blueprint(forum.forum)
app.register_blueprint(auth.auth)

if __name__ == '__main__':
    app.run(debug=True)

# flask shell
# >>> from app import db
# >>> db.create_all()