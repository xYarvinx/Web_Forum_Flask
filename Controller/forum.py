from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from Model.models import ForumPost, User

forum = Blueprint('forum', __name__)

@forum.route('/forum/<int:forum_id>')
def forum_details(forum_id):
    forum_data = ForumPost.query.get(forum_id)
    user_data = User.query.get(forum_data.user_id)
    return render_template('forum_details.html', forum=forum_data, user=user_data)


@forum.route('/')
def index():
    title = 'Главное меню'
    return render_template('index.html', title=title)

@forum.route('/forum')
def show_forum():
    forum_name = 'Форум'
    forums = ForumPost.query.all()  # Запрос для получения всех форумов из базы данных
    return render_template('forum.html', forum_name=forum_name, forums=forums)  # Передача списка форумов в шаблон

@forum.route('/forum/<int:forum_id>')
def forum_det(forum_id):
    forum_data = ForumPost.query.get(forum_id)
    user_data = User.query.get(forum_data.user_id)
    return render_template('forum_det.html', forum=forum_data, user=user_data)

@forum.route('/forum/<int:forum_id>/edit', methods=['GET', 'POST'])
def edit_forum(forum_id):
    forum_data = ForumPost.query.get(forum_id)
    if request.method == 'POST':
        # Обработка отправки формы для отредактированного поста
        forum_data.title = request.form['title']
        forum_data.content = request.form['content']
        db.session.commit()
        return redirect(url_for('forum.forum_det', forum_id=forum_data.id))
    return render_template('edit_forum.html', forum=forum_data)