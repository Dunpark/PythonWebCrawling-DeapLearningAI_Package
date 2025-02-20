############ 이런식으로 하면 인스타에서 계정 차단함 - 다른 방식으로 따오기

### 인스타그램 봇 만들기 1: 셀레니움 설치 / 간단한 수집
# 단순반복 웹업무 자동화하고 싶으면 
# 구조가 어려운 사이트 크롤링하고 싶으면
# -> Python + Selenium 활용 ==> request보다 간편하고 성공확률이 높음

## Selenium이랑 ChromeDriver 다운 받기
    # ChromeDriver의 경우 버전115이상은 모두 자신의 os에 맞게 다운받으면 됨
    # Selenium은 python 터미널에 pip install selenium을 실행시키면 됨

# 라이브러리 import
from selenium import webdriver
from selenium.webdriver.common.by import By # 업데이트 되어서 코딩애플이랑 다름름
from selenium.webdriver.common.keys import Keys
import time
import urllib.request #url(src)기반으로 이미지 가져오는 데 필요한 라이브러리

## 파이썬으로 브라우저부터 띄어보기
# 브라우저에서 하는 모든 웹작업들을 여기서 실행가능
# 웹페이지에서 데이터 수집도 쉽게 할 수 있음
# driver = webdriver.Chrome() # 처음 셋팅하는 코드
# driver.get('https://instagram.com') #인스타그램 페이지에 모든 데이터가 들어가 있음음 # 인스타 창이 실행되었다가 뒤에 더 명령 처리할 게 없으면 자동으로 꺼짐
# time.sleep(1000) # 프로그램의 실행을 () 안의 초만큼 멈춤
# 뜬 인스타그램 창에서 검사를 통해 원하는 데이터의 html상의 위치 찾기
# 관찰을 통해 원하는 글자 분석하여 class가 ~~인 글자를 찾게 코드 작성
#e = driver.find_element(By.CSS_SELECTOR, '.x5n08af') # 해당 함수를 작성해 찾아오라고 명령 # .class명을 작성해 class가 일치하는 데이터 추출 #업데이트 되어서 코딩애플이랑 다름 *대문자 주의
#print(e) #에러메시지가 자주 뜸 ex) no such element - 페이지 로딩시간 주의 --> time.sleep()을 사용하여 잠깐 찾을 시간 주기
#f = driver.find_element(By.CSS_SELECTOR, '.x5n08af').text # .text를 추가하면 텍스트 데이터만 추출됨
#print(f)

### 인스타그램 봇 만들기 2: 자동로그인하기
## Case study: 다른 것도 찾아보기

# html에서 스페이스를 포함한 긴 class명을 가진 코드들이 있었는데 얘네들이 여러 클래스를 의미하는 지 확인 --> .으로 교체해서 find_element하면 해당 데이터만 추출가능할 것임
#class_name = '.x2b8uid' # 클래스명이 여러개 부착되어 있다는 의미
#class_name = class_name.replace(' ', '.')
#f = driver.find_element(By.CSS_SELECTOR, class_name ).text
#print(f) # 정답 --> 맨 앞에 . 붙이고 replace 함수로 사이에 있는 공백을 .으로 변홚여 find_element()함수에 입력하기
# 아니면 마지막 class만 써도 ㄱㅊ --> 보통 class안에 포함된 class이기에 여러개가 나타남

# ID명에 기반해서 데이터 찾아오기 *ID는 페이지 내에서 하나밖에 존재할 수 없음
    # ID는 find_element() 함수에서 #ID명을 작성해서 넣으면 됨

# 속성(태그)으로도 찾을 수 있음 ex) Class나 ID와 같이 다른 추가 정보 없이 ~~=""로 되어 있는 html 요소
#e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]') # input[]로 감싸고 입력하면 됨 # <input> 태그라는 의미로 태그가 일치하는 것을 찾으라고 명령함 # 태그에 상응하는 값에 공백이 있으면 읽지 못함 --> .으로 처리
#print(e)

## 인스타그램 자동 로그인 하는 방법

driver = webdriver.Chrome() # 처음 셋팅하는 코드
driver.get('https://instagram.com') #인스타그램 페이지에 모든 데이터가 들어가 있음음 # 인스타 창이 실행되었다가 뒤에 더 명령 처리할 게 없으면 자동으로 꺼짐
time.sleep(3) # 페이지가 로드하는 데에 필요한 시간을 줌
# ID 입력
user_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]') # username_field = driver.find_element(By.NAME, "username")로도 가능
user_name_field.send_keys('dun_park2') # '내아이디'가 ID입력창에 자동입력됨
# 비밀번호 입력
password_field = driver.find_element(By.NAME, "password") # 비밀번호란을 지정함
password_field.send_keys('wildman2001!') # 비밀번호란에 입력
password_field.send_keys(Keys.ENTER) # Keys.하고 control + space를 누르면 브라우저에서 실행시킬 수 있는 동작들 목록이 나옴   # ex) Enters는 Enter키를 누르는 행위
time.sleep(10) # 위의 코드 실행 후 대기시간


## 다른 동작들 예시
#driver.find_element_by_css_selector('.class명').click() # 원하는 요소 클릭
# 가끔 click() 클릭이 안되면 강제클릭하는 법:
#e = driver.find_element_by_css_selector('클릭하고싶은요소')
#driver.execute_script('arguments[0].click();', e)


### 인스타그램 봇 만들기 3 : 페이지 이동과 이미지 수집

## 인스타그램 페이지에서 #사과 검색페이지의 이미지 수집
    # 무한스크롤의 형식으로 페이지가 구성되어 있음
## 사과 검색페이지의 이미지 수집 계획 - TIP. 코딩어떻게 할 지 모를 땐 한글부터 짜기
    # 1. 로그인 후 
    # 2. #사과 검색 페이지이동
    # 첫 사진 클릭
    # 이미지 저장
    # 다음 누르고 이미지 저장 *반복     

# 로그인 정보 기억하냐 마냐 뜨는 것 해결 - 클릭가능한 지 확인하는 방법: 웹 브라우저의 부분에 마우스를 갖다댔을 떄 ROle이 버튼이거나 key-board focusable할 때
e = driver.find_element(By.CSS_SELECTOR, '.xh8yej3')
driver.execute_script('arguments[0].click();', e) # 클릭이 잘 안될 떄에는 # execute_script:는 Javascript 실행 # arguments[0].click()는 강제클릭 # e는 대상
driver.implicitly_wait(10)

# 페이지 이동   *여러 줄 동시에 주석 처리하는 방법 : 영어로 타자설정 변환후 control + /
driver.get('https://www.instagram.com/explore/search/keyword/?q=%23%EC%82%AC%EA%B3%BC') #사과 검색페이지로 이동
time.sleep(5) # 만약 로딩이나 코드실행이 안되면 알아서 (최대)10초간 기다리라는 의미    *페이지 이동시에는 다시 작성해야 함


# # 첫째사진 누름
#     # 첫번째 사진의 class를 브라우저의 검사페이지에서 찾은 후 파이썬에서 가져오기
#         # class가 중복되어 있는 경우가 있으므로 꼭 html 검사페이지에서 찾아보기     ex) 1/28
# #pic1 = driver.find_element(By.CSS_SELECTOR, '_aagw').click() # class가 중복되어 있는 경우 가장 첫번째 자료 하나를 가져옴
# pic1 = driver.find_elements(By.CSS_SELECTOR, '._a6hd')[8].click() # find_elements()를 사용하면 class가 중복된 모든 자료를 리스트의 형식으로 가져옴  # 인덱싱을 통해 원하는 순서를 가져올 수 있음    # 모든 사진들은 대게 같은 class를 가지고 있으므로 2번째 자료는 2번째 게시물의 사진일 것임
# driver.implicitly_wait(10)
# # # 사진저장 - 이미지는 거의 <img>안에 있으므로 img태그 안의 src(이미지경로) 찾기
# 이미지 = driver.find_elements(By.CSS_SELECTOR, '.x87ps6o.xh8yej3')[8].get_attribute('src')
# urllib.request.urlretrieve(이미지, '사과_인스타게시글9_사진.jpg')     #urllib.request.urlretrieve(이미지URL, '파일명')
# time.sleep(3)

# # 게시글 나간 후 다음으로 이동
#     # 게시글 나가기
# out = driver.find_elements(By.CSS_SELECTOR, '.xurb0ha.xcdnw81')[1].click()
# driver.implicitly_wait(10)
#     # 다음 이동
# pic2 = driver.find_elements(By.CSS_SELECTOR, '._a6hd')[9].click() # find_elements()를 사용하면 class가 중복된 모든 자료를 리스트의 형식으로 가져옴  # 인덱싱을 통해 원하는 순서를 가져올 수 있음    # 모든 사진들은 대게 같은 class를 가지고 있으므로 2번째 자료는 2번째 게시물의 사진일 것임
# driver.implicitly_wait(10)
# # 사진저장
# 이미지 = driver.find_elements(By.CSS_SELECTOR, '.x87ps6o.xh8yej3')[9].get_attribute('src')
# urllib.request.urlretrieve(이미지, '사과_인스타게시글10_사진.jpg')     



## 10개의 게시물에서 사진을 가져오는 크롤러 + 사진이 아니면 무시(ex) 동영상은 pass)

for i in range(0,9):
    try:
        pic = driver.find_elements(By.CSS_SELECTOR, '._a6hd')[i].click() # find_elements()를 사용하면 class가 중복된 모든 자료를 리스트의 형식으로 가져옴  # 인덱싱을 통해 원하는 순서를 가져올 수 있음    # 모든 사진들은 대게 같은 class를 가지고 있으므로 2번째 자료는 2번째 게시물의 사진일 것임
        driver.implicitly_wait(10)
        # # 사진저장 - 이미지는 거의 <img>안에 있으므로 img태그 안의 src(이미지경로) 찾기
        이미지 = driver.find_elements(By.CSS_SELECTOR, '.x87ps6o.xh8yej3')[i].get_attribute('src')
        urllib.request.urlretrieve(이미지, f'사과_인스타게시글{i}_사진.jpg')     #urllib.request.urlretrieve(이미지URL, '파일명')
        time.sleep(3)
        # 게시글 나간 후 다음으로 이동
        out = driver.find_elements(By.CSS_SELECTOR, '.xurb0ha.xcdnw81')[1].click()
        driver.implicitly_wait(10)
    except:
        print(f'{i}게시물은 사진이 아닙니다')

## 시도해볼만한 추가 기능들
    # 댓글 작성하는 건 ID 작성하는 것이랑 똑같음 - 댓글알바 가능
    # 단시간에 너무 많이 수집하면 차단하는 사이트도 있음 주의

## 주의점:
    # 페이지 로딩시간이 부족하면 코드가 올바르게 작동하지 않을 가능성 높음 **driver.implicitly(10)써도 잘 안될 수 있음
    # 여러개의 요소로 이루어진 class같은 경우에 마지막 한 개만으로 차별화할 수 없을 가능성 많음 --> 마지막 2~3개정도 검색해보고 중복되는 지 확인
    # 클래스에 속해 있는 클래스 찾기: ('.클래스1 .클래스2') 넣기 
    # 중복되면 인덱싱으로 필요한 것들만 추출
    # 게시글의 특성상 사진만이 아니라 옆으로 넘기거나 동영상이 있는 경우도 있으니까 주의
    # 지정되는 요소 잘 보기

### 인스타그램 봇 만들기 4: 좋아요 & 댓글 자동화는?

