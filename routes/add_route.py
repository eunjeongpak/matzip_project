from flask import Blueprint, render_template, request

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/', methods=['GET'])
def add_index():
    return render_template('add.html'), 200


@bp.route('/submit', methods=['POST'])
def add_success():
    if request.method == 'POST':
        UserName = request.form.get('UserName')
        Name = request.form.get('Name')
        Address = request.form.get('Address')
        Address2 = request.form.get('Address2')
        Menu = request.form.get('Menu')
        Price = request.form.get('Price')

        if UserName == '' or Name == '':
            return render_template('add.html', message='Please enter required fields')

        return render_template('success.html'), 200

