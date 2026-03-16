# Tienda Online - Flask + Docker + Jenkins CI/CD

Aplicación web de ecommerce desarrollada en Python/Flask con pipeline CI/CD completo.

## Stack Tecnológico
- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Bootstrap
- **Base de datos:** SQLite
- **Contenedor:** Docker
- **CI/CD:** Jenkins + GitHub

## Pipeline CI/CD
```
git push → GitHub → Jenkins → Docker build → Deploy
```

## Funcionalidades
- Catálogo de productos
- Carrito de compras
- Login / Registro de usuarios
- Recuperación de contraseña

## Cómo correrlo localmente
```bash
pip install flask flask-login flask-sqlalchemy flask-mail werkzeug
python app.py
```

## Cómo correrlo con Docker
```bash
docker build -t tienda-online .
docker run -d -p 5000:5000 tienda-online
```
