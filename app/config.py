import os

# Определение базовой директории для проекта
basedir = os.path.abspath(os.path.dirname(__file__))

# Настройка секретного ключа
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

# Настройка URI для подключения к бд
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')


SQLALCHEMY_TRACK_MODIFICATIONS = False
