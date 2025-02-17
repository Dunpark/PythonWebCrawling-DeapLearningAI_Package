## 무신사의 전체리뷰 사이트를 들어갔을 때 내 키와 같은 리뷰들의 이미지 파일을 가져오는 크롤러 만들기

# 필요 라이브러리 
import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML_웹문서 분석을 도와주는 라이브러리 
import urllib.request # 이후 이미지URL을 활용해 이미지 파일로 저장할 떄 필요한 라이브러리
import re # url에서 제품번호 추출


numbers = re.findall(r'\d+', url)  # Finds all sequences of digits
print(numbers)  # Output: ['123', '456', '789']

def 맞춤형리뷰이미지(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')

https://goods.musinsa.com/api2/review/v1/view/list?page=1&pageSize=10&goodsNo=3674341&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false
https://goods.musinsa.com/api2/review/v1/view/list?page=2&pageSize=10&goodsNo=3674341&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false


