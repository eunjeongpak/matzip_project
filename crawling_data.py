# 데이터 크롤리애 csv로 저장

# 필요한 라이브러리
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
#######################################################
# 서울시 대학교 10개 리스트
# univ_list = ['서울대','연세대','고려대','서강대','성균관대','한양대','중앙대','경희대','외대','홍대']

# 1. 카카오맵 이동
url = "https://map.kakao.com/"
service = Service("C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

# 2. 음식점 입력 후 찾기 버튼 클릭
searchloc = input("univ_name")
filename = input("file_name")

search_area = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]')  # 검색 창
search_area.send_keys(searchloc)  # 검색어 입력
driver.find_element(By.XPATH, '//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter 검색
time.sleep(2)  # 일시 정지
driver.find_element(By.XPATH, '//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER) # 장소 버튼

# 3. 리스트 만들고 크롤링 함수 생성
list = []

def restaurant():
    time.sleep(0.2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    place_lists = soup.select('.placelist > .PlaceItem')

    count = 1
    for place in place_lists:
        temp = []

        place_name = place.select('.head_item > .tit_name > .link_name')[0].text
        place_category = place.select('.head_item > span')[0].text
        place_rating = place.select('.rating > .score > .num')[0].text
        place_review = place.select('.rating > .review > em ')[0].text
        place_link = place.select('.contact > .moreview')[0]['href']
        place_addr = place.select('.info_item > .addr > p')[0].text
        place_hour = place.select('.info_item > .openhour > p > a')[0].text
        place_tel = place.select('.info_item > .contact > span')[0].text

        print(place_name, place_category, place_rating, place_review, place_link, place_addr, place_hour, place_tel)

        temp.append(place_name)
        temp.append(place_category)
        temp.append(place_rating)
        temp.append(place_review)
        temp.append(place_link)
        temp.append(place_addr)
        temp.append(place_hour)
        temp.append(place_tel)

        list.append(temp)

    f = open(filename+'.csv', 'w', encoding='utf-8-sig', newline="")
    writercsv = csv.writer(f)
    header = ['name', 'category', 'rating', 'review', 'link', 'addr', 'hour', 'tel']
    writercsv.writerow(header)

    for i in list:
        writercsv.writerow(i)

# 크롤링 시작_1페이지부터 34페이지까지 출력
page = 1
page2 = 0
for i in range(0, 34):
    # 페이지 넘어가며 출력
    try:
        page2+=1
        print("**", page, "**")

        driver.find_element(By.XPATH, f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)
        restaurant()

        if (page2) % 5 == 0:
            driver.find_element(By.XPATH, '//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2 = 0

        page += 1
    except:
        break
print('크롤링 완료')