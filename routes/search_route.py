from flask import Blueprint, render_template, request, session
from run import db
from models.model import Restaurant
import pandas as pd
import folium
from folium.plugins import MarkerCluster

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
        # 음식점 지도 생성
        df = pd.read_csv("대학교.csv", encoding='utf-8')
        df = df[df['univ'] == univ_name]

        map = folium.Map(location=[37.541, 126.986], zoom_start=12)
        marker_cluster = MarkerCluster().add_to(map)

        for index, a in df.iterrows():
            if float(a["rating"]) >= 4:#평점 4점 이상 빨간색
                color = "red"

            elif float(a["rating"]) >= 3:#평점 3점 이상 주황색
                color = "orange"

            else:#평점 3점 미만
                color = "lightgreen"

            print_popup = str(a["name"]) + "<br> 카테고리 : " + str(a["category"]) + "<br> 평점 : " + str(a["rating"]) + \
                          " <br> 리뷰수 : " + str(a["review"]) + "<br> 주소 : " + str(a["addr"]) + "<br>" + '<a href="' + str(a["link"]) + '" target="_self">' + str(a["link"]) + '</a>'

            folium.Marker(location=[a["lat"], a["lng"]],
                          popup=print_popup, icon=folium.Icon(color=color)).add_to(marker_cluster)

        html_map = map._repr_html_()
        data = Restaurant.query.filter_by(univ=univ_name).all()
        return render_template('result.html', data=data, map=html_map)





