### 응용연습
## H.W 사과 검색했을 때 100개의 게시물을 가져오는 크롤러 만들어보기
#Ans
'''
# 필요한 라이브러리 가져오기
import requests 
from bs4 import BeautifulSoup

scope = [1, 31, 61, 91] # 데이터 추출 범위지정하기 *나중에 세부사항 추가
count = 0 #100까지 세기
for i in scope: # 각 페이지 범위에 공통적으로 적용되는 for루프 만들기
    data = requests.get(f'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start={i}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') 
    리스트 = soup.select('a.title_link') # 예를 들어 i가 1이면 1부터 30번까지의 게시물 제목이 리스트에 포함됨
    for j in 리스트: # 리스트 안의 요소들을 하나하나 다루는 for 루프 생성
        count+=1
        print(j.text) # 제목 출력
        if count == 100: # 데이터 추출 범위 100개로 한정시키기
            break # for루프 진행을 멈추게 하는 코드
'''


## 네이버블로그순위를 보여주는 함수 만들어주기 - 검색어에 따라 뜨는 게시물 순위
    # get 링크에서 'query='가 검색어를 뜻하고 & 기호는 구분을 위해 사용됨
    # 근데 파이썬에서 query부분이 이상하게 뜨는 이유는 한국어 인코딩이 다르기 떄문. 한국어로 입력해도 상관없음
# Ans

# 필요한 라이브러리 가져오기 # 파이썬 실행 시 항상 커널이 재시작되어서 이전코드 메모처리하면 새로 라이브러리를 가져와야 함함
import requests 
from bs4 import BeautifulSoup
# 검색어를 입력값으로 가지며 그에 따라 100개의 검색순위를 추출하는 함수 만들기

def 검색순위():
    검색어 = input()
    count=0
    scope = [1, 31, 61, 91] # 데이터 추출 범위지정하기 *나중에 세부사항 추가
    textfile = open(f'{검색어}순위100.txt', 'w', encoding='utf-8') # Windows 는 기본적으로 CP494 인코딩을 사용하는데 한국어는 포함X -> 인코딩 바꿔주기
    for i in scope: # 각 페이지 범위에 공통적으로 적용되는 for루프 만들기
        data = requests.get(f'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query={검색어}&start={i}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
        soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') 
        리스트 = soup.select('a.title_link') # 예를 들어 i가 1이면 1부터 30번까지의 게시물 제목이 리스트에 포함됨
        for j in 리스트: # 리스트 안의 요소들을 하나하나 다루는 for 루프 생성
            count+=1
            textfile.write(f'{count}. {j.text}\n')
            if count == 100: # 데이터 추출 범위 100개로 한정시키기
                textfile.close()
                break # for루프 진행을 멈추게 하는 코드`
검색순위()