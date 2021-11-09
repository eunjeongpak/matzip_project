# 크롤링으로 준비된 csv 데이터 전처리 및 postgresql 데이터베이스에 넣기

# 데이터프레임 업로드 -> 합치기
# datashape = (5008, 9)
import pandas as pd
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

# 평점이 0인 음식점 제거
# datashape = (3478, 9)
idx = df[df['rating']==0].index
df.drop(idx, inplace=True)

# 중복값 확인 및 제거
# datashape = (3459, 9)
duplicate_rows = df[df.duplicated()]
df = df.drop_duplicates(keep='first')
df = df.reset_index(drop=True)

# 데이터베이스 연결
from sqlalchemy import create_engine
engine = create_engine('postgresql://bihifqmu:bQVDAoxN9Wc8FHqIYoDVJDoR3bpO5QHx@rosie.db.elephantsql.com/bihifqmu')

df.to_sql("univ_res", engine)
