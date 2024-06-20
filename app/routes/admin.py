from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from app.models import User, Product


# Пример защиты маршрутов с использованием декоратора login_required
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Логика административной панели
    return render_template('admin/dashboard.html', title='Административная панель')
