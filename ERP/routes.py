from routes import *

from flask import redirect, render_template, request, url_for
from app import app,db
from models import Inventory

@app.route('/')
def dashboard():
    return render_template('base.html')

@app.route('/inventory')
def inventory():
    items = Inventory.query.all()
    return render_template('inventory/inventory.html',inventory=items)

@app.route('/add_inventory', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_item = Inventory(name=name, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('inventory'))
    return render_template('inventory/add_inventory.html')

@app.route('/edit_inventory/<int:id>', methods=['GET', 'POST'])
def edit_inventory(id):
    item = Inventory.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.quantity = request.form['quantity']
        db.session.commit()
        return redirect(url_for('inventory'))
    return render_template('inventory/edit_inventory.html',item=item)

@app.route('/delete_inventory/<int:id>')
def delete_inventory(id):
    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('inventory'))

