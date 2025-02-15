### 무한 스크롤러 데이터 수집 1(네이버 블로그)

# 페이지에 따라 나뉘어져 있는 경우 --> URL 활용(page = )
    # URL이 어떤 양상으로 변화하는 지 알면 맞춰서 크롤러를 만들기가 쉬움

# 무한스크롤인 경우(계속 내릴 수 있는 경우)
    # 그냥 get방법으로는 첫 페이지만 수집가능
    # --> 추가데이터들을 달라고 네이버 서버에 요청하기
        # 개발자도구에서 네트워크 탭에 들어가기
        # 이 페이지를 보여주기 위해 서버에서 받아온 모든 파일 들이 뜸
        # 여기서 더보기 데이터 찾아보기
        # 더보기 데이터가 담긴 파일을 찾은 후 그걸 서버에 따로 요청하면 크롤러 가능
            # 개발자도구의 화면에서 게시물의  control + f로 제목 검색해서 추가된 데이터 찾기
            # 뜨는 결과에서 Headers 탭이 제일 중요함
                # 추가된 데이터파일이 어떠한 경로를 통해 get요청할 수 있는 지 나와있음
                # 이전에 배운 requests.get요청이 결국 서버에 get요청하는 것과 동일한 방식으로 기능
#EX)
import requests 
from bs4 import BeautifulSoup
# 첫번쨰 도착한 더보기 게시물
#requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=61&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
# 두번째 도착한 더보기 게시물
#requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=91&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=90&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
    # -> 둘의 url을 비교하면 start에서 차이가 있음을 알 수 있음
    # -> 첫번째는 61부터 90번까지, 두번쨰는 91부터 120번까지 가져온다는 것을 유추할 수 잇음
# 이와 같이 url의 특징을 활용해 for loop을 기반으로 무한 스크롤 데이터 수집 가능


### 무한 스크롤러 데이터 수집 2(네이버 블로그)

## 더보기 게시물의 데이터 가져오기
requests.get('A%B3%BC&start=61&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') # class명에 백슬래시가 들어가있는 경우가 잇음 -> 가져올 때 오류가 나므로 모든 \ 삭제하기    #replace(대상, 결과)   # replace는 text를 대상으로 하기 때문에 get.text 활용 -> 데이터를 문자형식으로 가져옴
# 위 코드에서 \를 한번 쓰면 특수한 기호를 의미하고 두번 적어야 글자로 인식됨  

# 브라우저에 개발자도구를 활용해 필요한 데이터 파악하기
# HTML에서 원하는 정보 뽑으려면 select 쓰기
#print(soup.select('a.title_link')) # a라는 태그 + title_link라는 클래스    # 각 게시물들의 제목만을 뽑아옴
리스트 = soup.select('a.title_link') 
#print(리스트[0].text) # text를 써야 텍스트 데이터가 나옴
#print(리스트[1].text)
#print(리스트[2].text)

print(리스트[0]['href']) # href는 링크로 이처럼 href 인덱싱가능
print(리스트[1]['href'])
print(리스트[2]['href'])

## 1~30, 31~ 60, 원하는 구간의 데이터를 추출하려면 'start = ' 부분에서 입력을 다르게 하는 for loop을 생성하면 됨 *이미지 수집도 가능
data = requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=61&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')