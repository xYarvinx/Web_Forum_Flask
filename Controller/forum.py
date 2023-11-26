#forum.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import *

from forms import CreatePostForm, CreateCommentForm, EditPostForm
from app import db
from Model.models import User, ForumPost, Comment

forum = Blueprint('forum', __name__)

@forum.route('/forum/<int:post_id>', methods=['GET', 'POST'])
def forum_details(post_id):
    forum_data = ForumPost.query.get(post_id)
    user_data = User.query.get(forum_data.user_id)
    comments = (db.session.query(Comment, User).filter_by(post_id=post_id).filter_by(user_id=User.id)
                .order_by(-Comment.id).values(User.username, Comment.text,
                                              User.id.label('user_id'), Comment.id.label('comment_id')))

    # оставление комментариев
    form = CreateCommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.content.data, user_id=current_user.id, post_id=forum_data.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('forum.forum_details', post_id=forum_data.id))

    return render_template('forum_details.html', forum=forum_data, user=user_data,
                           comments=comments, form=form)

@forum.route('/')
def index():
    title = 'Главное меню'
    return render_template('index.html', title=title)

@forum.route('/forum')
def show_forum():
    forum_name = 'Форум'
    forums = ForumPost.query.all()  # Запрос для получения всех форумов из базы данных
    return render_template('forum.html', forum_name=forum_name, forums=forums)  # Передача списка форумов в шаблон

@login_required
@forum.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = ForumPost(title=form.title.data, content=form.content.data, user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('forum.show_forum'))
    return render_template('create_post.html', form=form)

@login_required
@forum.route('/forum/<int:post_id>/edit_post/', methods=['GET', 'POST'])
def edit_post(post_id):

    post = ForumPost.query.get_or_404(post_id)
    form = EditPostForm()
    if current_user.id != post.user_id:
        return redirect(url_for('forum.forum_details', forum_id=post.id))
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('forum.forum_details', forum_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('edit_forum.html', form=form, post=post)

@login_required
@forum.route('/forum_details/<int:comment_id>', methods=['GET','DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post = ForumPost.query.get_or_404(comment.post_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('forum.forum_details', forum_id=post.id))


@login_required
@forum.route('/forum/<int:post_id>/delete_post', methods=['POST', 'GET'])
def delete_post(post_id):
    if request.method == 'GET':
        post = ForumPost.query.get_or_404(post_id)
        if current_user.id != post.user_id:
            return redirect(url_for('forum.forum_details', forum_id=post.id))

        # Querying and deleting comments related to the post
        comments = Comment.query.filter_by(post_id=post_id)
        for comment in comments:
            db.session.delete(comment)

        # Deleting the post
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('forum.show_forum'))

    return redirect(url_for('forum.show_forum'))


