from datetime import datetime
from app import db

# Модель User для таблицы пользователей в бд
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор пользователя
    username = db.Column(db.String(64), index=True, unique=True)  # Имя пользователя
    email = db.Column(db.String(120), index=True, unique=True)  # Email пользователя
    password_hash = db.Column(db.String(128))  # Хеш пароля пользователя

    def __repr__(self):
        return f'<User {self.username}>'  # Строковое представление объекта User


# Модель Post для таблицы постов в бд
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор поста
    title = db.Column(db.String(140))  # Заголовок поста (до 140 символов)
    content = db.Column(db.Text)  # Содержание поста
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # Время создания поста
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Внешний ключ на id пользователя, который создал пост

    def __repr__(self):
        return f'<Post {self.title}>'  # Строковое представление объекта Post
