from flask import Blueprint, render_template
from models.producto import Producto

tienda = Blueprint('tienda', __name__)

@tienda.route('/')
def catalogo():
    productos = Producto.query.all()
    return render_template('tienda/catalogo.html', productos=productos)

@tienda.route('/producto/<int:id>')
def detalle(id):
    producto = Producto.query.get_or_404(id)
    return render_template('tienda/producto.html', producto=producto)
