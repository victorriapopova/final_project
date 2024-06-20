from flask import render_template, flash, redirect, url_for
from app import app, db  # Импорт экземпляра приложения Flask и экземпляра SQLAlchemy
from app.forms import LoginForm, PostForm  # Импорт классов форм для входа и создания поста
from app.models import User, Post  # Импорт моделей User и Post


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    # Запрос всех постов из базы данных
    posts = Post.query.all()
    return render_template('index.html', title='Главная',
                           posts=posts)  # Рендеринг шаблона index.html с передачей списка постов


# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Создание экземпляра формы LoginForm

    if form.validate_on_submit():  # Если форма отправлена и данные прошли валидацию
        user = User.query.filter_by(
            username=form.username.data).first()  # Поиск пользователя по имени пользователя из формы
        if user is None or not user.check_password(
                form.password.data):  # Проверка наличия пользователя и соответствия пароля
            flash('Неправильное имя пользователя или пароль')  # Вывод сообщения об ошибке
            return redirect(url_for('login'))  # Перенаправление на страницу входа

        flash('Успешная авторизация!')  # Вывод сообщения об успешной авторизации
        return redirect(url_for('index'))  # Перенаправление на главную страницу

    return render_template('login.html', title='Вход', form=form)  # Рендеринг шаблона login.html с передачей формы


# Страница создания поста
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()  # Создание экземпляра формы PostForm

    if form.validate_on_submit():  # Если форма отправлена и данные прошли валидацию
        post_ = Post(title=form.title.data, content=form.content.data)  # Создание нового объекта поста
        db.session.add(post_)  # Добавление поста в сессию базы данных
        db.session.commit()  # Фиксация изменений в базе данных
        flash('Пост опубликован!')  # Вывод сообщения об успешном создании поста
        return redirect(url_for('index'))  # Перенаправление на главную страницу

    return render_template('post.html', title='Новый пост', form=form)  # Рендеринг шаблона post.html с передачей формы
