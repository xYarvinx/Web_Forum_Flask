#forms.py
from wtforms import PasswordField,StringField, SubmitField
from wtforms.validators import EqualTo, Email, DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class CreatePostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Создать пост')

class EditPostForm(FlaskForm):
        title = StringField('Заголовок', validators=[DataRequired()])
        content = TextAreaField('Содержание', validators=[DataRequired()])
        submit = SubmitField('Сохранить изменения')

class CreateCommentForm(FlaskForm):
    content = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Оставить комментарий')




