from flask import Blueprint, render_template, session, redirect, url_for
from models.producto import Producto

carrito = Blueprint('carrito', __name__)

@carrito.route('/carrito')
def ver():
    ids = session.get('carrito', [])
    items = []
    for pid in ids:
        producto = Producto.query.get(pid)
        if producto:
            items.append(producto)
    total = sum(p.precio for p in items)
    return render_template('carrito/carrito.html', items=items, total=total)

@carrito.route('/agregar/<int:id>')
def agregar(id):
    cart = session.get('carrito', [])
    cart.append(id)
    session['carrito'] = cart
    return redirect(url_for('carrito.ver'))

@carrito.route('/eliminar/<int:id>')
def eliminar(id):
    cart = session.get('carrito', [])
    if id in cart:
        cart.remove(id)
    session['carrito'] = cart
    return redirect(url_for('carrito.ver'))

@carrito.route('/vaciar')
def vaciar():
    session['carrito'] = []
    return redirect(url_for('carrito.ver'))
