from flask import Flask
from config import Config
from models import db, login_manager
from routes.auth import auth
from routes.tienda import tienda
from routes.carrito import carrito

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Registrar blueprints (modulos de rutas)
    app.register_blueprint(auth)
    app.register_blueprint(tienda)
    app.register_blueprint(carrito)

    # Crear tablas si no existen
    with app.app_context():
        from models.usuario import Usuario
        from models.producto import Producto
        from models.orden import Orden, ItemOrden
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
