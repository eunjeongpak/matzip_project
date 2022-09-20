# matzip_project
  - 작성자 : 박은정
  - 작성날짜 : 2021/12/07
  - GITHUB : https://github.com/eunjeongpak/matzip_project
 
### 프로젝트 주제
    Flask를 활용해 서울시 대학교 맛집 추천 서비스 <UNIV_MATZIP> 웹 구축 프로젝트
    
### 프로젝트 결과물 
    https://matzipapp.herokuapp.com/
    현재 서비스 UI 개선을 위한 일시적인 점검 중입니다 
    
### 프로젝트 목적
    대학교 주변 맛집 데이터를 크롤링해 서울시 10개 대학교 주변 맛집 관련 데이터 제공 및 추천시스템을 통한 추천 서비스 제공

### 프로젝트DB 설계_Postgresql
  ![image](https://user-images.githubusercontent.com/76864400/144953861-989c306e-237d-482e-96dd-0fba46a49dc5.png)
  
    크롤링한 데이터는 univ_restaurant table에 저장, 사용자가 추가(수정or삭제)할 수 있는 데이터는 univ_new에 저장
    
### 프로젝트 분석 방법 및 내용 
  1. selenium 활용해 카카오맵에서 데이터 웹 크롤링해 데이터 수집
    ![image](https://user-images.githubusercontent.com/76864400/142368454-9128e314-23b9-48dc-b807-ffad80c628f2.png)
    
      - 프로젝트에 사용한 데이터: 카카오맵으로 크롤링한 서울시 10개 대학교 주변 맛집 데이터
      - 출처: https://map.kakao.com/
      - selenium을 활용해 서울대학교, 연세대학교, 고려대학교, 서강대학교, 성균관대학교, 한양대학교, 중앙대학교, 경희대학교, 한국외국어대학교, 홍익대학교 주변 맛집을 크롤링
     

  2. 크롤링한 데이터 전처리 후 postgresql 데이터베이스에 저장
    ![image](https://user-images.githubusercontent.com/76864400/141224642-0ff09948-7428-40d4-8a07-e2c81d06cb07.png)
    
  3. FLASK를 활용해 웹 애플리케이션 구축
    ![image](https://user-images.githubusercontent.com/76864400/142368911-e388b318-8edb-47e7-ac25-87791b2d7591.png)

  4. FLASK와 Postgresql 데이터베이스 연결해 웹 CRUD 구현
    ![image](https://user-images.githubusercontent.com/76864400/142374867-9e4f8074-86cb-4edd-a2a9-2392fd6c97a8.png)
    ![image](https://user-images.githubusercontent.com/76864400/142375045-8ac9c94a-ac63-4a8c-acbf-bed8b7055635.png)


  5. folium 사용해 웹에서 맛집 지도 시각화
    ![image](https://user-images.githubusercontent.com/76864400/142374969-675463f6-fc70-4ea6-822d-edd5daa01fa0.png)

  
  6. 추천시스템 구축
    ![image](https://user-images.githubusercontent.com/76864400/144954181-58d209e6-d626-43f5-b8da-d5c0182eb36d.png)
    ![image](https://user-images.githubusercontent.com/76864400/144954315-6b43491a-c4cc-4f13-bddd-b1722c4ca57f.png)


  7. 헤로쿠 배포
      
    

### 프로젝트 사용 언어: python








