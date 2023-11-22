from flask import Blueprint, render_template, request, redirect, url_for
from app import app, db
from Model.models import ForumPost, User
from forms import CreatePostForm
from Model.models import Post
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

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    form = CreatePostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('forum'))
    posts = Post.query.all()
    return render_template('forum_details.html', form=form, posts=posts)
