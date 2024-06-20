from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


# Форма для входа пользователя
class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])  # Поле для ввода имени пользователя
    password = PasswordField('Пароль', validators=[DataRequired()])  # Поле для ввода пароля
    submit = SubmitField('Войти')


# Форма для создания нового поста


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])  # Поле для ввода заголовка поста
    content = StringField('Содержание', validators=[DataRequired()])  # Поле для ввода содержания поста
    submit = SubmitField('Опубликовать')
