from werkzeug.security import generate_password_hash, check_password_hash


# Хеширование пароля
def hash_password(password):
    """
    Принимает пароль в виде строки и возвращает его хешированную версию
    """
    return generate_password_hash(password)


# Проверка пароля
def verify_password(hashed_password, password):
    """
    Принимает хешированный пароль и пароль в виде строки,
    и возвращает True, если пароль совпадает с хешем, иначе False
    """
    return check_password_hash(hashed_password, password)


import random
import string


def generate_random_string(length=12):
    """
    Генерирует случайную строку заданной длины, состоящую из букв и цифр
    """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
