# ### 그 유명한 이동평균선으로 시계열 데이터 분석하는 법

# ## 주식데이터 기반으로 시각화 연습해보기


# # 필요한 라이브러리 가져오기
# import pandas as pd
# import yfinance as yf   # 야후만 가능
#     # pip install yfinance를 통해 설치 
# import FinanceDataReader as fdr     # 네이버랑 KRX에서 정보를 가져옴
#     # pip install finance-datareader를 통해 설치 
# # 필요한 주가데이터 불러오기
# df1 = yf.download("AAPL", start='2019-09-10', end='2020-10-09') # 종목:애플
# #print(df)

# #df['Close'] # 종가(그날의 마지막 가격) 
# #print(df1['Close'].plot())  # 콜럼하나만 출력하만 시리즈 데이터로 시리즈데이터는 .plot()로 차트(linegraph) 생성 가능
#     # *로컬 컴퓨터에선 안나옴 --> google colab 사용해야 함' / matplotlib 라이브러리 사용
#     # .plot()은 데이터가 숫자일때만 적용 가능

# df2 = fdr.DataReader('NAVER:005930', start='2019-09-10', end='2020-10-09')  # 005930 = 삼성전자 코드
# print(df2)      # dataframe엔 index 컬럼이 존재할 수 있음
# print(df2.index)    # 날짜를 인덱스로 함

# # 주의점: 주식데이터값이 숫자처럼 생겼지만 숫자자료가 아닐 수 있음
# df2['Close'] = df2['Close'].astype(float)   #를 통해 데이터형식을 바꾼 자료 덮어쓰기

# ## 시계열데이터(time series)를 다룰 때 이동평균선을 자주 활용함 - 5일간 가격을 평균내서 그래프로 그린 것    ex) 1-5 평균, 2-6 평균, 3-7 평균 ...과 같이 점을 찍어 그래프 생성 *꼭 5일 기준X
#     # ex) 5일간과 60일기준의 이동평균선을 보았을 떄 교차지점에서 주식을 구매하면 이득을 본다는 식으로 이론을 세움
#     # 하루 가격은 변동이 심한데 이동평균선을 통해 일별 노이즈를 제거해 주가의 전체적인 흐름 및 추세를 확인할 수 있음
# # 이동평균선 그리는 방법
# df2['Close'].rolling(5).mean()  # 5개씩 잡아서 평균을 내줌
# df2['Close'].rolling(20).sum() # 합계도 가능 *20기준으로
# df2['rolling5'] = df2['Close'].rolling(5).mean() # 새로운 컬럼에 이동평균선 수치 추가
# print(df2)


# ### 데이터 시각화에 Matplotlib 자주쓰니까 필요한 내용 빠른 정리 - 이미 배운 내용이랑 많이 겹치므로 강의 텍스트 기반 정리
# import matplotlib.pyplot as plt
'''
# 일단 pip install matplotlib으로 설치부터 하시면 됩니다. 

## 간단한 선그래프 그리는 법 
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [11,12,13,14,15])
plt.show()
plt.plot() 한줄 쓰면 선그래프를 그려줍니다. 그리고 show()하면 보여줍니다. 

plot()함수 안엔 X축데이터들, Y축데이터들을 차례로 리스트자료로 입력해주시면 됩니다. 

예를 들어 위의 코드에선 (1,11) (2,12) (3,13) .. 이런 좌표를 연결하는 선을 그려줍니다. 

심지어는 판다스 column을 직접 입력해도 그려줍니다.

판다스 컬럼 하나도 리스트랑 비슷한 취급을 받아서 그렇습니다. 

plt.plot(df.index, df['Close'])
plt.show()
이렇게 가능합니다. df는 저번시간데 받아왔던 주식가격 데이터입니다.
 

## 차트에 라벨을 달고 싶은 경우 

plt.plot(df.index, df['Close'], color="crimson")
plt.xlabel('time')
plt.ylabel('price')
plt.legend(['apple'])
plt.show() 
plot() 안의 color 파라미터엔 선색상도 집어넣을 수 있고

xlabel()은 가로축 

ylabel()은 세로축

legend()는 범례를 맘대로 이름지을 수 있습니다. (리스트 자료가 들어갑니다)

참고로 plt.figure(figsize=(10,10)) 이걸 plt.plot()하기 전에 적어주시면 차트사이즈를 좀 키울 수 있습니다. (10,10) 안에 inch단위로 가로세로 사이즈를 적어주시면 됩니다. 

 

## 선그래프를 동시에 여러개 띄우고 싶으면

plt.plot([1,2,3], [10,20,30])
plt.plot([1,2,3], [30,60,90])
plt.show() 
plot()을 여러번 쓰면 됩니다. 한 차트에 선을 여러개 그려줍니다. 

 
## 바차트를 그리고 싶으면 

plt.bar(['A','B','C'], [10,20,30])
plt.show() 
bar()를 쓰면 됩니다. 

역시 X축, Y축에 들어갈 데이터를 리스트로 쭉 넣어주면 됩니다. 

바차트는 연속된 time series 데이터가 아닐 경우, X축이 카테고리 데이터일 경우 보통 사용합니다. 
 

## 파이차트를 그리고 싶으면 

plt.pie([5,10,15])
plt.show() 
pie()를 사용하고 안에 데이터들만 쭉 리스트로 담아주면 됩니다. 

그럼 각 데이터들이 얼마나 차지하는지의 비율을 파이차트로 보여줍니다. 


## 히스토그램을 그리고 싶으면 

 

plt.hist([160,161,168,165,169,170,171,172,180])
plt.show() 
hist()를 사용하고 데이터들만 넣으면 됩니다.

히스토그램은 어떤 데이터가 빈출하는지 나타낼 때 사용합니다.

전국 남자 키 분포 이런거 나타내고싶을 때 그리면 좋겠군요. 

hist() 여기도 역시 판다스 컬럼 하나 집어넣어도 잘 보여줍니다. 


## 분포도(scatterplot)를 그리고 싶으면 

math = [5,8,23,5,67,34,34,23]
eng = [23,6,3,1,5,45,54,34]
plt.scatter(math, eng)
plt.show() 
scatter()를 쓰신 다음 X축, Y축 데이터를 차례로 적습니다. 

이건 언제 쓰냐면 X데이터와 Y데이터 간의 상관관계를 살펴보고 싶을 때 혹은 분포를 보고 싶을 때 사용합니다. 

위의 예제에선 1번부터 8번 학생의 수학성적, 영어성적을 각각 리스트로 정리해놓고 그걸 scatterplot으로 그려본 겁니다.

그럼 수학성적이 높으면 영어성적도 높은지 경향성을 분석해볼 수 있겠죠? 

(하지만 그래프 하나는 인과관계를 설명해주진 않습니다.)

 
## 스택차트를 그리고 싶으면 

plt.stackplot(['A','B','C'], [10,20,30], [30,20,50], [10,20,30])
plt.show() 
stackplot(X축, Y축1, Y축2, Y축3 ... ) 이걸 사용합니다. 

stackplot은 Y축데이터를 여러개 집어넣을 수 있으며 그럼 여러개의 선을 그려줍니다. 

근데 선을 위로 쌓아서 그려줍니다. 그래서 누적데이터를 살펴보고 싶을 때 그리면 좋습니다. 

위의 예제는 예를 들어 사원 3명의 A,B,C상품 판매데이터를 누적해서 보여주는 그래프라고 생각하면 쉽겠네요. 

첫 사원은 [10,20,30] 만큼 팔았고 둘째 사원은 [30,20,50] 만큼 판겁니다. 

이걸 누적차트로 표현하면 총 판매량을 한눈에 볼 수 있겠네요. 

 

## (오늘의 간단 숙제)

Q. 원하는 데이터만 보이게 그래프를 조작하고 싶습니다. 

yahoo에서 2020년 01월01일~12월31일의 비트코인 가격을 가져오고 Close 가격을 그래프로 그리고 싶습니다. (종목코드 BTC-USD)

근데 Volume항목 2020년의 평균Volume보다 높은 날의 가격만 그래프로 그려보고 싶은데 어떻게 코드를 짜야할까요? 

 
A.
(결과 예시입니다. 전 심심해서 bar 차트로 그려봤습니다)

이건 답이지만 그 전에 구글 검색찬스도 있습니다

데이터 가져오는 방법은 설명 생략해도 되겠죠? 

그리고 Volume 항목의 평균을 출력해봤습니다. 궁금해서요.  

import pandas as pd
from pandas_datareader import data

df = data.DataReader('BTC-USD','yahoo', start="2020-01-01", end="2020-12-31")
평균 = df['Volume'].mean()
print(평균)
  

그 다음 새로운 컬럼을 만들었습니다. 평균값보다 높으면 True, 아니면 False를 저장해주는 tf라는 이름의 컬럼입니다. 

그 다음 조건문을 이용해 df['tf'] 안에 들어있는 값이 True 인 행만 출력하는 새로운 a라는 데이터프레임을 만들었습니다. 

import pandas as pd
from pandas_datareader import data

df = data.DataReader('BTC-USD','yahoo', start="2020-01-01", end="2020-12-31")
평균 = df['Volume'].mean()
print(평균)

df['tf'] = df['Volume'] > 평균
print(df)
a = df[df['tf']==True]
print(a)
 

그 다음에 a라는 데이터프레임에 있는 항목 중 'Close' 컬럼만 차트로 그려봤다고합니다. 

bar 차트를 이용했습니다. 

import pandas as pd
from pandas_datareader import data

df = data.DataReader('BTC-USD','yahoo', start="2020-01-01", end="2020-12-31")
avg = df['Volume'].mean()
print(avg)

df['tf'] = df['Volume'] > avg
print(df)

a = df[df['tf']==True]
print(a)


import matplotlib.pyplot as plt
plt.bar(a.index, a['Close'])
plt.show() 
 
'''
# Failed
'''
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 데이터 다운로드 (auto_adjust=False 설정)
df = yf.download('BTC-USD', start="2020-01-01", end="2020-12-31", auto_adjust=False)

# 평균 거래량 계산 (Series 형태가 아닌 float 값으로 변환)
avg = df['Volume'].mean()
print("평균 거래량:", avg)

# 평균 거래량 초과 여부 컬럼 추가
df['tf'] = df['Volume'] > avg

# 평균 거래량 초과 데이터 필터링
a = df[df['tf']]

# 날짜 데이터를 숫자로 변환
dates = mdates.date2num(a.index.to_numpy())  

# 종가 데이터를 float 형태로 유지 (정수 변환 X)
b = a['Close'].values.astype(float)

# 그래프 출력
plt.figure(figsize=(12, 6))
plt.bar(dates, b, width=1.5, color='blue', alpha=0.7)

# x축 날짜 포맷 설정
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Bitcoin Close Prices on High Volume Days")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
'''