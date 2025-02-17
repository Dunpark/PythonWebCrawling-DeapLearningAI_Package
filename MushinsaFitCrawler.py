## 무신사 제품페이지를 들어갔을 때 내 키와 같은 리뷰들의 이미지 파일을 가져오는 크롤러 만들기

# 필요 라이브러리 
import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML_웹문서 분석을 도와주는 라이브러리 
import urllib.request # 이후 이미지URL을 활용해 이미지 파일로 저장할 떄 필요한 라이브러리
import re # url에서 제품번호 추출



print(numbers)  # Output: ['123', '456', '789']

def 맞춤형리뷰이미지(url):
    product_id = re.findall(r'\d+', url)[0]  # 모든 연속된 숫자들(숫자모음)을 리스트에 추출 --> 하나인 경우 인덱싱으로 텍스트 데이터 추출가능
    for page from range(0,100):
        data=requests.get(f'https://goods.musinsa.com/api2/review/v1/view/list?page={}&pageSize=10&goodsNo={}&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false')
        soup = BeautifulSoup(data.content, 'html.parser')
        

https://goods.musinsa.com/api2/review/v1/view/list?page=1&pageSize=10&goodsNo=3674341&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false
https://goods.musinsa.com/api2/review/v1/view/list?page=2&pageSize=10&goodsNo=3674341&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false


