from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import db
from models.usuario import Usuario
import secrets

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect(url_for('tienda.catalogo'))
        flash('Email o contraseña incorrectos', 'error')
    return render_template('auth/login.html')

@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        if Usuario.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'error')
            return redirect(url_for('auth.registro'))
        nuevo = Usuario(nombre=nombre, email=email)
        nuevo.set_password(password)
        db.session.add(nuevo)
        db.session.commit()
        flash('Cuenta creada exitosamente', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/registro.html')

@auth.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        email = request.form.get('email')
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            token = secrets.token_urlsafe(32)
            usuario.token_recuperacion = token
            db.session.commit()
            # Aqui iria el envio de email con Flask-Mail
            flash('Te enviamos un email para recuperar tu contraseña', 'success')
        else:
            flash('Email no encontrado', 'error')
    return render_template('auth/recuperar.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
