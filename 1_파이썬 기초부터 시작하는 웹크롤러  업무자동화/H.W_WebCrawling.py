## H.W 
'''
종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']
주식 종목코드를 기반으로 종목들의 현개가격을 .txt파일에 저장 되도록 하는 코드 작성성
'''

## My Ans
#필요한 라이브러리 import
import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup

# 리스트 변수에 담기
list = ['005930', '066575', '005380', '035720', '034220', '003490']

# URL이 바뀌는 부분을 입력하면 해당 종목의 현재가격을 불러오는 함수 작성성
def 현재가upg(구멍): # URL이 바뀌는 부분을 기입가능한 변수로 만들어 다양한 기업의 가격수집에 활용할 수 있게 함
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={구멍}') 
    soup = BeautifulSoup(데이터.content, 'html.parser')
    hw.write(f"\n{soup.find_all('strong', id='_nowVal')[0].text}")

# for루프를 활용해 자동으로 list 내의 요소들을 함수에 입력 및 실행
for i in list: 
    if i == list[0]: # 시작에 텍스트파일 생성
        hw = open('hw.text', 'w')
    현재가upg(i)
    if i == list[-1]:
        hw.close() # 마지막에 텍스트파일 닫기

## Teacher's Ans
# range 활용용
종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

f = open('a.txt', 'w')
for i in range(6):
  f.write( '\n' + 현재가( 종목들[i] ) )

f.close()


# list 활용
종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']
f = open('a.txt', 'w')
for i in 종목들: 
  f.write( '\n' + 현재가( i ) )
f.close()
