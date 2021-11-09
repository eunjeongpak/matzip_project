from flask import Blueprint, render_template
from sqlalchemy import desc

from run import db
from models.model import Restaurant

bp = Blueprint('list', __name__, url_prefix='/list')

@bp.route('/', methods = ["GET"])
def list_index():
    return render_template('search.html')

@bp.route('/result', methods = ["GET"])
def list_result():
    # list = Restaurant.query.order_by(Restaurant.index).all()
    data = Restaurant.query.filter_by(univ='서울대학교').order_by(desc(Restaurant.rating)).all()
    return render_template('list.html', data=data)