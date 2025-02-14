### 응용연습
## H.W 사과 검색했을 때 100개의 게시물을 가져오는 크롤러 만들어보기

data = requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=61&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=60&ngn_country=KR&lgl_rcode=02290107&fgn_region=&fgn_city=&lgl_lat=37.43319&lgl_long=126.993374&enlu_query=IggCAF6CULjEAAAAf0OW4HuKSDHwdp9uf%2FQoPsP5%2F6m%2B99%2FPmzQh7XVW0ACJJWp9oGWOE9RvbI9xfCIhtRdntOGegAKietw9i36ZTQJ6GI4xyDalFFZWXVF1bgYapvZlbi48f5o0qW3Wdpnh%2BtmZScvnV%2FHT6Qgk3jskkdzaBqUz4xUnn1Sssvik52E%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt=')
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') 

## 네이버블로그순위를 보여주는 함수 만들어주기 - 검색어에 따라 뜨는 게시물 순위
    # get 링크에서 'query='가 검색어를 뜻하고 & 기호는 구분을 위해 사용됨
    # 근데 파이썬에서 query부분이 이상하게 뜨는 이유는 한국어 인코딩이 다르기 떄문. 한국어로 입력해도 상관없음

