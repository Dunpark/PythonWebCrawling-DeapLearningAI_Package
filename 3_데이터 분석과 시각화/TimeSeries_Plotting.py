### 그 유명한 이동평균선으로 시계열 데이터 분석하는 법

## 주식데이터 기반으로 시각화 연습해보기


# 필요한 라이브러리 가져오기
import pandas as pd
import yfinance as yf   # 야후만 가능
    # pip install yfinance를 통해 설치 
import FinanceDataReader as fdr     # 네이버랑 KRX에서 정보를 가져옴
    # pip install finance-datareader를 통해 설치 
# 필요한 주가데이터 불러오기
df1 = yf.download("AAPL", start='2019-09-10', end='2020-10-09') # 종목:애플
#print(df)

#df['Close'] # 종가(그날의 마지막 가격) 
#print(df1['Close'].plot())  # 콜럼하나만 출력하만 시리즈 데이터로 시리즈데이터는 .plot()로 차트(linegraph) 생성 가능
    # *로컬 컴퓨터에선 안나옴 --> google colab 사용해야 함' / matplotlib 라이브러리 사용
    # .plot()은 데이터가 숫자일때만 적용 가능

df2 = fdr.DataReader('NAVER:005930', start='2019-09-10', end='2020-10-09')  # 005930 = 삼성전자 코드
print(df2)      # dataframe엔 index 컬럼이 존재할 수 있음
print(df2.index)    # 날짜를 인덱스로 함

# 주의점: 주식데이터값이 숫자처럼 생겼지만 숫자자료가 아닐 수 있음
df2['Close'] = df2['Close'].astype(float)   #를 통해 데이터형식을 바꾼 자료 덮어쓰기

## 시계열데이터(time series)를 다룰 때 이동평균선을 자주 활용함 - 5일간 가격을 평균내서 그래프로 그린 것    ex) 1-5 평균, 2-6 평균, 3-7 평균 ...과 같이 점을 찍어 그래프 생성 *꼭 5일 기준X
    # ex) 5일간과 60일기준의 이동평균선을 보았을 떄 교차지점에서 주식을 구매하면 이득을 본다는 식으로 이론을 세움
    # 하루 가격은 변동이 심한데 이동평균선을 통해 일별 노이즈를 제거해 주가의 전체적인 흐름 및 추세를 확인할 수 있음
# 이동평균선 그리는 방법
df2['Close'].rolling(5).mean()  # 5개씩 잡아서 평균을 내줌
df2['Close'].rolling(20).sum() # 합계도 가능 *20기준으로
df2['rolling5'] = df2['Close'].rolling(5).mean() # 새로운 컬럼에 이동평균선 수치 추가
print(df2)


### 데이터 시각화에 Matplotlib 자주쓰니까 필요한 내용 빠른 정리
