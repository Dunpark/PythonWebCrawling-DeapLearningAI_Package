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
driver = webdriver.Chrome() # 처음 셋팅하는 코드
driver.get('https://instagram.com') #인스타그램 페이지에 모든 데이터가 들어가 있음음 # 인스타 창이 실행되었다가 뒤에 더 명령 처리할 게 없으면 자동으로 꺼짐
time.sleep(2) # 프로그램의 실행을 () 안의 초만큼 멈춤
# 뜬 인스타그램 창에서 검사를 통해 원하는 데이터의 html상의 위치 찾기
# 관찰을 통해 원하는 글자 분석하여 class가 ~~인 글자를 찾게 코드 작성
#e = driver.find_element(By.CSS_SELECTOR, '.x5n08af') # 해당 함수를 작성해 찾아오라고 명령 # .class명을 작성해 class가 일치하는 데이터 추출 #업데이트 되어서 코딩애플이랑 다름 *대문자 주의
#print(e) #에러메시지가 자주 뜸 ex) no such element - 페이지 로딩시간 주의 --> time.sleep()을 사용하여 잠깐 찾을 시간 주기
#f = driver.find_element(By.CSS_SELECTOR, '.x5n08af').text # .text를 추가하면 텍스트 데이터만 추출됨
#print(f)

## html에서 스페이스를 포함한 긴 class명을 가진 코드들이 있었는데 얘네들이 여러 클래스를 의미하는 지 확인 --> .으로 교체해서 find_element하면 해당 데이터만 추출가능할 것임
class_name = '.x5n08af x1f6kntn xcxhlts x1jqylkn x1fqp7bg x13ibhcj x2b8uid'
class_name = class_name.replace(' ', '.')
f = driver.find_element(By.CSS_SELECTOR, class_name ).text
print(f) # 정답 --> 맨 앞에 . 붙이고 replace 함수로 사이에 있는 공백을 .으로 변홚여 find_element()함수에 입력하기


### 인스타그램 봇 만들기 2: 자동로그인하기기
# 