from flask import Blueprint, render_template

from Model.models import ForumPost


forum = Blueprint('forum', __name__)

from flask import render_template

@forum.route('/forum/<int:forum_id>')
def forum_details(forum_id):
    # Логика для отображения информации о конкретном форуме (forum_id)
    forum_data = ForumPost.query.get(forum_id)  # Здесь вы можете использовать функцию для извлечения данных о форуме из базы данных или другого источника
    return render_template('forum_details.html', forum=forum_data)

@forum.route('/')
def index():
    title = 'Главное меню'
    return render_template('index.html', title=title)

@forum.route('/forum')
def show_forum():
    forum_name = 'Форум'
    forums = ForumPost.query.all()  # Запрос для получения всех форумов из базы данных
    return render_template('forum.html', forum_name=forum_name, forums=forums)  # Передача списка форумов в шаблон
