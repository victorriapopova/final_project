from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создание экземпляра Flask
app: Flask = Flask(__name__)

# Настройка параметров приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Создание экземпляра SQLAlchemy, связанного с приложением Flask
db = SQLAlchemy(app)
