from flask import Blueprint, render_template, request, session
from sqlalchemy import desc
from run import db
from models.model import Restaurant

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods = ["GET"])
def list_index():
    return render_template('search.html')

@bp.route('/result', methods = ['GET', 'POST'])
def list_result():
    univ = session.get('univ')
    univ_name = request.args.get('univ_name')

    if univ_name is None:
        return "대학교 이름을 입력하세요", 400

    elif Restaurant.query.filter_by(univ=univ_name).first() is None:
        return f"{univ_name} not in database", 404

    else:
        data = Restaurant.query.filter_by(univ=univ_name).all()
        return render_template('result.html', data=data)
