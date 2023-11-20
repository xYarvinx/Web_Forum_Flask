from flask import Blueprint, render_template
forum = Blueprint('forum', __name__)

@forum.route('/')
def index():
    title = 'Главное меню'
    return render_template('index.html', title=title)

@forum.route('/forum')
def show_forum():
    forum_name = 'Форум'
    return render_template('forum.html', forum_name=forum_name)
