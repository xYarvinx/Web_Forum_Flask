from Model.models import User
from app import app, db


@app.before_first_request
def seed_data():
    # Пример добавления данных
    user1 = User(username='example1', email='example1@email.com')
    user1.password = 'qwerty1234'
    user2 = User(username='example2', email='example2@email.com')
    user2.password = 'yuiop2345'
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
