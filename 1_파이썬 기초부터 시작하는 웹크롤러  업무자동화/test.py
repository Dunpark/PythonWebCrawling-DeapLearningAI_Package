import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML_웹문서 분석을 도와주는 라이브러리 
import urllib.request # 이후 이미지URL을 활용해 이미지 파일로 저장할 떄 필요한 라이브러리
import re # url에서 제품번호 추출


url = 'https://www.musinsa.com/products/3674341'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
product_id = re.findall(r'\d+', url)[0]  # 모든 연속된 숫자들(숫자모음)을 리스트에 추출 --> 하나인 경우 인덱싱으로 텍스트 데이터 추출가능
data=requests.get(f'https://goods.musinsa.com/api2/review/v1/view/list?page=1&pageSize=10&goodsNo={product_id}&sort=up_cnt_desc&selectedSimilarNo=3674341&myFilter=false&hasPhoto=false&isExperience=false', headers=headers)
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
image_urls = soup[0]
# Convert relative URLs to absolute URLs (assuming base URL is known)
print(image_urls)

# Print the extracted image URLs


'''
## 더보기 게시물의 데이터 가져오기
data = requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=61&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') # class명에 백슬래시가 들어가있는 경우가 잇음 -> 가져올 때 오류가 나므로 모든 \ 삭제하기    #replace(대상, 결과)   # replace는 text를 대상으로 하기 때문에 get.text 활용 -> 데이터를 문자형식으로 가져옴
# 위 코드에서 \를 한번 쓰면 특수한 기호를 의미하고 두번 적어야 글자로 인식됨  

# 브라우저에 개발자도구를 활용해 필요한 데이터 파악하기
# HTML에서 원하는 정보 뽑으려면 select 쓰기
#print(soup.select('a.title_link')) # a라는 태그 + title_link라는 클래스    # 각 게시물들의 제목만을 뽑아옴
리스트 = soup.select('a.title_link') 
print(리스트)
print(리스트[0].text) # text를 써야 텍스트 데이터가 나옴
print(리스트[1].text)
print(리스트[2].text)
'''