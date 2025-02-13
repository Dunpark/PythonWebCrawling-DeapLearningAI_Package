### Naver의 정보를 가져오는 crawler 생성
## 사전작업 *만약 시행안되면 1. python 설치 시 pip 체크박스 해제해서 2. 윈도의 경우 python -m pip install requests로 작성해서 실행해 보기 3. 윈도우의 경우 허가되지 않은 script 실행 막았다고 에러 뜨면 컴퓨터 시작화면에서 powershell을 관리자권한으로 실행 후 Set-ExecutionPolicy Unrestricted 실행
    # 터미널에 pip install requests 실행
    # pip install bs4 실행
import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML_웹문서 분석을 도와주는 라이브러리 

##크롤러의 프로세스:

# 1. 파이썬으로 데이터 들어있는 웹사이트 접속(그럼 HTML 도착)
데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930') # 해당 웹페이지 정보가 변수에 다 들어감 *requests() 복수형 주의
    #네이버 금융웹사이트에서 데이터 가져옴
'''
print(데이터) #데이터가 수집되었는 지 확인 -> 'Response [200]'과 같이 출력되었으면 성공적임
print(데이터.content) # 그 웹페이지에 들어있던 모든 HTML 데이터
print(데이터.status_code) # 사이트 데이터를 제대로 가져왔는 지 검사 --> 200이 출력되면 성공적, 400이 뜨면 차단이 되었거나 URL을 잘못 쓰는 등 실패했음을 의미
'''


soup = BeautifulSoup(데이터.content, 'html.parser') # html데이터를 읽기 용이하게 정리해줌 #*html 데이터를 다루는 것이므로 첫째 항에 .content가 붙어야함  # 이쁜 html을 soup라고 부름
# print(soup)


# 2. HTML 속에서 필요한 정보만 빼오기
# 터미널에서 보긴 힘드니까 크롬과 같은 인터넷 브라우저로 웹사이트 에 들어가 개발자도구를 클릭해 html 요소 파악
# 개발자도구 창의 맨 위의 왼쪽 끝을 보면 사각형을 클릭하는 아이콘이 있는데 이 아이콘을 누르고 웹사이트의 정보에 마우스를 갖다 대면 해당 정보가 HTML 코드의 어디에 위치해 있는 지를 보여줌
# 데이터가 어디에 위치해 있는 지 파악하면 파이썬으로 html 중 해당 부분을 찾아달라는 코드를 작성하면 됨
    # 태그의 class랑 id는 이름과 마찬가지임
    # id = ''를 찾아달라는 코드를 작성하면 해당 이름을 가진 데이터를 가져옴
print(soup.find_all('strong', id="_nowVal")) # print(soup.find_all('태그명', 속성명)) # 해당 데이터가 속해있는 구간을 의미 = html 코드의 시작부분# 속성은 class나 id와 같은 이름을 의미함
    # 찾은 결과는 리스트의 형식으로 가져옴
print(soup.find_all('strong', id="_nowVal")[0]) #인덱싱을 해야 리스트 안의 결과만 가져옴 *리스트 안에 요소가 하나가 있으므로
print(soup.find_all('strong', id="_nowVal")[0].text) # html요소관련정보를 제외하고 text정보만 가져옴 
# 만약 clss로 찾고 싶으면 calss_=""로 적어야 함
# 만약 class명이 두개라면 하나만 적어야 함 ex) 개발자도구 화면에서 class = "tah p11"로 나와 있으면 tah와 pll이라는 두개의 클라스를 가진다는 의미
    
# class랑 id로 찾을 떄의 차이점: 
    # id는 유니크해서 html마다 고유id가 있음
    # class는 중복가능함
        # soup.find._all은 해당 class를 지닌 모든 데이터를 가져오기 때문에 인덱싱을 통해 같은 class 내에서 또 어떤 기준으로 데이터들이 구분되는 지 파악해야 함
            # ex) print(soup.find_all('strong', class_="tah")[0].text) -> 여러가지 데이터가 출력되지만 같은 다른 기준으로 같은 카테고리에 있는 것들임
        # --> 그러므로 class로 찾을 때에는 리스트 인덱싱을 잘해주어야 함





# Notes
'''
pip는 라이브러리를 설치할 때 쓰는 것으로 다른 사람이 만들어놓은 기능모음들을 가져오는 것임
  


'''