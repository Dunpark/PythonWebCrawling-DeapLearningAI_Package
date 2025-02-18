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
## 파이썬으로 브라우저부터 띄어보기
# 브라우저에서 하는 모든 웹작업들을 여기서 실행가능
# 웹페이지에서 데이터 수집도 쉽게 할 수 있음
#driver = webdriver.Chrome() # 처음 셋팅하는 코드
#driver.get('https://instagram.com') #인스타그램 페이지에 모든 데이터가 들어가 있음음 # 인스타 창이 실행되었다가 뒤에 더 명령 처리할 게 없으면 자동으로 꺼짐
#time.sleep(10) # 프로그램의 실행을 () 안의 초만큼 멈춤
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
'''
driver = webdriver.Chrome() # 처음 셋팅하는 코드
driver.get('https://instagram.com') #인스타그램 페이지에 모든 데이터가 들어가 있음음 # 인스타 창이 실행되었다가 뒤에 더 명령 처리할 게 없으면 자동으로 꺼짐
time.sleep(5) # 페이지가 로드하는 데에 필요한 시간을 줌
# ID 입력
user_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]') # username_field = driver.find_element(By.NAME, "username")로도 가능
user_name_field.send_keys('dun_park2') # '내아이디'가 ID입력창에 자동입력됨
# 비밀번호 입력
password_field = driver.find_element(By.NAME, "password") # 비밀번호란을 지정함
password_field.send_keys('비밀번호입력') # 비밀번호란에 입력
password_field.send_keys(Keys.ENTER) # Keys.하고 control + space를 누르면 브라우저에서 실행시킬 수 있는 동작들 목록이 나옴   # ex) Enters는 Enter키를 누르는 행위
time.sleep(10) # 위의 코드 실행 후 대기시간
'''

## 다른 동작들 예시
#driver.find_element_by_css_selector('.class명').click() # 원하는 요소 클릭
# 가끔 click() 클릭이 안되면 강제클릭하는 법:
#e = driver.find_element_by_css_selector('클릭하고싶은요소')
#driver.execute_script('arguments[0].click();', e)


### 인스타그램 봇 만들기 3 : 페이지 이동과 이미지 수집
import urllib.request #이건 import 모여있는 맨위에다가 작성
urllib.request.urlretrieve(이미지URL, '파일명')