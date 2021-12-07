from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.model import Restaurant, New_restaurant
from run import db

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/')
def add_index():
    return render_template('add.html'), 200

@bp.route('/add_res')
def add_res():
    return render_template('add_res.html'), 200

@bp.route('/success', methods=['POST'])
def add_success():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        address = request.form['addr']
        university = request.form['univ']

        if name == '' or category == '' or address == '' or university == '':
            return render_template('add.html', message='Please enter required fields')

        else:
            if db.session.query(Restaurant).filter(Restaurant.name == name).first() == None:
                new = New_restaurant(name=name,
                                     category=category,
                                     addr=address,
                                     univ=university)
                db.session.add(new)
                db.session.commit()

            else:
                pass

        return render_template('success.html'), 200

@bp.route('/add_list')
def add_list():
    data = New_restaurant.query.all()
    return render_template('add_list.html',data=data), 200

@bp.route('/add_list/update', methods = ['GET', 'POST'])
def add_list_update():
    if request.method == 'POST':
        data = New_restaurant.query.get(request.form.get('id'))

        data.name = request.form['name']
        data.category = request.form['category']
        data.addr = request.form['addr']
        data.univ = request.form['univ']

        db.session.commit()

        return redirect(url_for('add.add_list'))

@bp.route('add_list/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    data = New_restaurant.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return redirect(url_for('add.add_list'))
