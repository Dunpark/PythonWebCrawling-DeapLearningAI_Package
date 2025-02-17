#### Naver의 정보를 가져오는 crawler 생성

### 웹클롤러 1 강의 - 파이썬으로 웹페이지 접속과 원하는 글자 찾기
## 사전작업 *만약 시행안되면 1. python 설치 시 pip 체크박스 해제해서 2. 윈도의 경우 python -m pip install requests로 작성해서 실행해 보기 3. 윈도우의 경우 허가되지 않은 script 실행 막았다고 에러 뜨면 컴퓨터 시작화면에서 powershell을 관리자권한으로 실행 후 Set-ExecutionPolicy Unrestricted 실행
    # 터미널에 pip install requests 실행
    # pip install bs4 실행
import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML_웹문서 분석을 도와주는 라이브러리 
import urllib.request # 이후 이미지URL을 활용해 이미지 파일로 저장할 떄 필요한 라이브러리

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
#print(soup.find_all('strong', id="_nowVal")) # print(soup.find_all('태그명', 속성명)) # 해당 데이터가 속해있는 구간을 의미 = html 코드의 시작부분# 속성은 class나 id와 같은 이름을 의미함
    # 찾은 결과는 리스트의 형식으로 가져옴
#print(soup.find_all('strong', id="_nowVal")[0]) #인덱싱을 해야 리스트 안의 결과만 가져옴 *리스트 안에 요소가 하나가 있으므로
#print(soup.find_all('strong', id="_nowVal")[0].text) # html요소관련정보를 제외하고 text정보만 가져옴 
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


### 웹클롤러 2 강의 - 혼자 코드짤 때 도움되는 case study
## 특수한 형태의 html 코드들을 다루는 방법
# 1. HTML 상으로 글자가 해체되어 있는 경우:
    # 모든 글자가 포함된 class를 기준으로 검색하면 됨
# 2. calss, id하나도 없는 요소:
    # select() 활용 --> css 셀렉터 입력해서 원하는 html 찾기 가능
#soup.select('.f_down')  # = class가 f_down인 것을 찾아주세요. --> class는 .
#soup.select('#_nowVal') # = id가 _nowVal인 것을 찾아주세요
#soup.select('strong#_NowVal') # = 태그가 strong이면서 id가 _nowVal인 것을 찾아주세요
    # 정리하면 class = ., id = #, tag는 그대로, 두개 만족하려면 이어어쓰기
        #-> class와 태그를 기준으로 찾을 수 있음
#soup.select('.f_down em') # 띄어쓰는 것은 내부요소를 의미하는 것으로 f_down 클래스 안에 있는 em 태그에 사응하는 데이터를 가져오라는 것  #얘도 인덱싱 가능
    # 치트키로 웹페이지 검사에서 찾고자 하는 데이터에 마우스 우클릭으로 copy selecter를 선택하면 경로를 복사할 수 있음
#soup.select('tab_con1 > div:nth-child(6) > table > tbody > tr:nth-child(2) > td > em')
# 3. 이미지 수집방법
    # 이미지는 id = img임
#이미지 = soup.select('#middle > div.h_company > div.wrap_company > div > img')[0] # [0]을 붙여야 리스트가 아닌 텍스트 데이터로 가져옴
#print(이미지)
    #이미지의 html 요소들 중에서 src는 이미지의 주소로 가장 중요한 데이터임
#print(이미지['src']) # 추출한 데이터 중 src만 선택하여 추출
#urllib.request.urlretrieve(이미지['src'], '코스피') # src를 활용해 해당 이미지를 '코스피'라는 이미지파일로 컴퓨터에 저장
# 4. 다른 종목 가격들 수집도 동시에 하려면? = 대용량 크롤러?
    # 반복문 활용
        # 하나의 웹사이트에서 뻗어나오는 웹사이트들이 URL만 살짝 다름
        # 같은 특징을 지닌 데이터는 웹사이트가 다르더라도 ID나 Class가 같을 확률이 높음

### 웹클롤러 3 강의 - 함수활용해서 자동화 시키기
## H.W 함수 문법을 적용해 긴 코드 축약해보기
def 현재가():# 삼성전자 가격 수집 # 포함시키고 있는 코드는 모두 인덴트시키기
    데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930') # 삼전 종목코드
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    print(soup.find_all('strong', class_="tah")[5].text)
## 함수 업그레이드 시키기 --> 함수에 기입가능한 변수 만들기
def 현재가upg(구멍): # URL이 바뀌는 부분을 기입가능한 변수로 만들어 다양한 기업의 가격수집에 활용할 수 있게 함
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={구멍}') # 삼전 종목코드 # 이때 f는 formatting을 의미
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    print(soup.find_all('strong', class_="tah")[0].text)
    return soup.find_all('strong', id="_nowVal")[0].text # 함수실행한 자리에 결과물(현재가격)을 남김
    #방법2: 리스트.append(soup.find_all('strong', id="_nowVal")[0].text) #리스트에 데이터가 저장되어 언제든 필요한 데이터를 부를 수 있음

#현재가upg('005930') # 삼성전자 가격 데이터
#현재가upg('066575') # LG 가격 데이터

## 방법1: 파일에 출력한 데이터 저장시키기 
f = open('a.txt', 'w')
f.write(현재가upg('005930'))
f.write(현재가upg('066575'))
f.close()

##방법2: #위에서 만든 리스트를 기반으로 인덱싱해서 f.write