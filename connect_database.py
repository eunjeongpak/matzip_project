# 크롤링으로 준비된 csv 데이터 전처리 및 postgresql 데이터베이스에 넣기
import pandas as pd
import googlemaps

# 데이터프레임 업로드 -> 합치기 -> datashape = (5008, 9)
df_서울대 = pd.read_csv('서울대학교.csv')
df_서울대['univ'] = '서울대학교'
df_연세대 = pd.read_csv('연세대학교.csv')
df_연세대['univ'] = '연세대학교'
df_고려대 = pd.read_csv('고려대학교.csv')
df_고려대['univ'] = '고려대학교'
df_서강대 = pd.read_csv('서강대학교.csv')
df_서강대['univ'] = '서강대학교'
df_성균관대 = pd.read_csv('성균관대학교.csv')
df_성균관대['univ'] = '성균관대학교'
df_한양대 = pd.read_csv('한양대학교.csv')
df_한양대['univ'] = '한양대학교'
df_중앙대 = pd.read_csv('중앙대학교.csv')
df_중앙대['univ'] = '중앙대학교'
df_경희대 = pd.read_csv('경희대학교.csv')
df_경희대['univ'] = '경희대학교'
df_외대 = pd.read_csv('한국외국어대학교.csv')
df_외대['univ'] = '한국외국어대학교'
df_홍대 = pd.read_csv('홍익대학교.csv')
df_홍대['univ'] = '홍익대학교'

df = pd.concat([df_서울대, df_연세대, df_고려대, df_서강대, df_성균관대, df_한양대, df_중앙대, df_경희대, df_외대, df_홍대])

# 평점이 0인 음식점 제거 -> datashape = (3478, 9)
idx = df[df['rating']==0].index
df.drop(idx, inplace=True)

# 중복값 확인 및 제거 -> datashape = (3459, 9)
duplicate_rows = df[df.duplicated()]
df = df.drop_duplicates(keep='first')
df = df.reset_index(drop=True)

# 데이터프레임에 위경도 컬럼 추가
API_KEY = "AIzaSyA21irbuBCrP6TZZRH6UjiXr0Wfw9v5OtY" # 구글맵 키
gmaps = googlemaps.Client(key=API_KEY)

# 위도, 경도
lat = []
lng = []

# 우리나라 위경도 최대 최소값
max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0

# 위경도 추가
for place in df["addr"]:
    tmp = gmaps.geocode(place, language="ko")

    # 구글맵 검색
    if tmp:
        tmp_loc = tmp[0].get("geometry")
        tmp_lat = tmp_loc["location"]["lat"]
        tmp_lng = tmp_loc["location"]["lng"]

        # 우리나라 위도 경도 값 안에 들어있지 않으면
        if (tmp_lat > max_lat or tmp_lat < min_lat or tmp_lng > max_lng or tmp_lng < min_lng):
            lat.append("0")
            lng.append("0")

        # 우리나라 위도 경도 값 안에 들어있으면
        else:
            lat.append(tmp_lat)  # 위도 추가
            lng.append(tmp_lng)  # 경도 추가

    # 검색 안 될 경우 0으로 입력
    else:
        lat.append("0")
        lng.append("0")

print("위경도 추가 완료")

# list를 데이터 프레임으로 변경 및 열 이름 변경
df2 = pd.DataFrame(lat)
df2 = df2.rename(columns={0: "lat"})
df3 = pd.DataFrame(lng)
df3 = df3.rename(columns={0: "lng"})

# dataframe 3개 합치고 위경도 0인 행 삭제 -> datashape = (3459, 11)
df = pd.concat([df, df2, df3], axis=1)
df = df.query("lat != '0'")

# 최종 csv로 저장
df.to_csv("대학교.csv", encoding="utf-8-sig")

# 데이터베이스 연결
from sqlalchemy import create_engine
engine = create_engine('postgresql://bihifqmu:bQVDAoxN9Wc8FHqIYoDVJDoR3bpO5QHx@rosie.db.elephantsql.com/bihifqmu')

df.to_sql("univ_restaurant", engine)
