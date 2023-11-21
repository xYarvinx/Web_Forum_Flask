# fill_db.py
from app import db,app
from Model.models import User, ForumPost, Comment
from werkzeug.security import generate_password_hash

def populate_database():
    with app.app_context():
    # Добавление пользователей
        user1 = User(username='user1', email='user1@example.com')
        user1.password_hash = generate_password_hash('password1')  # Устанавливаем хэш пароля
        user2 = User(username='user2', email='user2@example.com')
        user2.password_hash = generate_password_hash('password2')  # Устанавливаем хэш пароля

    # Добавление записей на форуме
        post1 = ForumPost(title='First Post', content='This is the content of the first post.', user=user1)
        post2 = ForumPost(title='Second Post', content='Content for the second post.', user=user2)

    # Добавление комментариев
        comment1 = Comment(text='This is a comment.', forum_post=post1, user=user2)
        comment2 = Comment(text='Another comment here.', forum_post=post1, user=user1)

    # Добавление объектов в сессию и сохранение в БД
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(comment1)
        db.session.add(comment2)
        db.session.commit()

if __name__ == '__main__':
   populate_database()
