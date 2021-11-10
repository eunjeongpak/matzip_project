import pandas as pd
import folium
import webbrowser
from folium.plugins import MarkerCluster

# 음식점 지도 생성
df = pd.read_csv("대학교.csv", encoding='utf-8')

map = folium.Map(location=[37.5642135, 127.0016985], zoom_start=10)
marker_cluster = MarkerCluster().add_to(map)

for index, a in df.iterrows():
    # 평점 4점 이상 빨간색
    if float(a["rating"]) >= 4:
        score_color = "red"

    # 평점 3점 이상 주황색
    elif float(a["rating"]) >= 3:
        score_color = "orange"

    # 평점 3점 미만
    else:
        score_color = "lightgreen"

    print_popup = str(a["name"]) + "<br> 평점 : " + str(a["rating"]) + " <br> 리뷰수 : " + str(
        a["review"]) + "<br> 주소 : " + str(a["addr"]) + "<br>" + '<a href="' + str(
        a["link"]) + '" target="_self">' + str(a["link"]) + '</a>'

    folium.Marker(location=[a["lat"], a["lng"]],
                  popup=print_popup, icon=folium.Icon(color=score_color)).add_to(marker_cluster)

map.save('selectWestern.html')

# 웹에 띄워줌
# webbrowser.open('selectWestern.html')