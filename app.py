from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/oteba/PycharmProjects/flaskProject/Forumdb'
db = SQLAlchemy(app)

from Controller import forum, auth  # Import after db is defined to avoid circular imports

app.register_blueprint(forum.forum)
app.register_blueprint(auth.auth)

if __name__ == '__main__':
    with app.app_context():  # Use app_context() to ensure proper context initialization
        db.create_all()
    app.run(debug=True)

# flask shell
# >>> from app import db
# >>> db.create_all()