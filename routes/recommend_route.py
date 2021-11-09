from flask import Blueprint, render_template

bp = Blueprint('recommend', __name__, url_prefix='/recommend')

@bp.route('/')
def rec_index():
    return render_template('recommend.html'), 200
