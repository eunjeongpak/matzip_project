from flask import Blueprint, render_template, request
from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도
import pandas as pd
import numpy as np

bp = Blueprint('recommend', __name__, url_prefix='/recommend')

@bp.route('/', methods=["GET"])
def rec_index():
    return render_template('recommend.html'), 200

@bp.route('/result', methods=["GET"])
def rec_result():
    keyword = request.args.get('res_name')

    # 데이터프레임 업로드
    df = pd.read_csv('대학교.csv')
    # 카테고리, 대학교 묶어주기
    df['recommend'] = df['category'] + df['univ']

    # 코사인 유사도 사용해 추천시스템 구축
    # 데이터 간의 text feature 벡터라이징
    count_vect_category = CountVectorizer(min_df=0, ngram_range=(1, 2))
    place_category = count_vect_category.fit_transform(df['recommend'])
    # 텍스트 간의 코사인 유사도 따지기
    place_simi_cate = cosine_similarity(place_category, place_category)

    # 최종 추천시스템 구축
    # * 0.003 등의 가중치를 줘서 조절
    place_simi_co = (
            + place_simi_cate * 0.3  # 카테고리 유사도
            + np.repeat([df['rating'].values], len(df['rating']), axis=0) * 0.005  # rating이 얼마나 높은지
    )
    place_simi_co_sorted_ind = place_simi_co.argsort()[:, ::-1]

    # 최종 구현 함수
    def find_simi_place(df, sorted_ind, place_name, top_n=10):
        place_title = df[df['name'] == place_name]
        place_index = place_title.index.values
        similar_indexes = sorted_ind[place_index, :(top_n)]
        similar_indexes = similar_indexes.reshape(-1)
        return df.iloc[similar_indexes]

    data = find_simi_place(df, place_simi_co_sorted_ind, keyword, 5)
    data = pd.DataFrame(data=data)
    return render_template('recommend_result.html', keyword=keyword,  tables=[data.to_html(classes='data')], titles=data.columns.values)

