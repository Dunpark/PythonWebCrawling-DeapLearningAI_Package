### Pandas 1 : 엑셀은 느려 SQL은 어려워 그러면 판다스로 통계내십시오
## Python을 잘하면 엑셀의 고급기능활용과 대용량 데이터를 다룰 수 있음

# pandas 설치하기: 터미널에 pip install pandas 입력 
# 라이브러리 불러오기
import pandas as pd
# csv 파일 가져오기
df = pd.read_csv(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\credit.csv')
#print(df)
# # 한 column의 평균 구해보기 - ex) 나이 평균
# print(df['나이'].mean()) # 원하는 column 가져와서 .mean() 적용
# # 최빈값 구해보기
# print(df['나이'].mode()) # 원하는 column 가져와서 .mode() 적용
# # 최댓값 구해보기
# print(df['나이'].max())  # .max()
# # 최솟값 구해보기
# print(df['나이'].min())  # .min()
# # 기본적인 stat들을 한번에 출력할 수 있음
# print(df['나이'].describe())    # .describe()

# 판다스에서 다루는 dataframe 자료형(2차원 데이터 - 행렬데이터)이니까 df라고 부름
# Series 자료형: 1차원 데이터로 리스트와 동일함

# # 카테고리에 따라 분석해보기
# print((df.groupby('성별').mean(numeric_only=True)))   # df.groupby('컬럼명')    # 성별 카테고리에 따라 나머지 데이터가 평균값으로 묶임
    # 평균으로 묶여지기 위해서는 수치 데이터여야 함 --> (numeric_only=True) 파라미터 추가 


### Pandas 2 : query 주기 & 리스트자료 dataframe으로 변환 & 숙제

## correlation값 구하기 - 정수들이 들어 있는 column 2개(이상도 가능)를 정해야 함
    # 나이와 사용금액에 대한 상관성 분석
#print(df[['나이', '사용금액']].corr())    # df[컬럼1, 컬럼2].corr()  # 0과 1 사이의 수치로 결과 출력됨

## 원하는 데이터만 필터주기
#print(df[ df['나이'] > 50]) # df[조건입력가능] : df에서 나이 콜럼의 값들 중 50보다 큰 값들의 df의 형식으로 출력한다는 의미

## 필터에 여러가지 조건식을 한번에 주고 싶을 때
# 나이가 50보다 많고 결혼한 사람들의 데이터만 필터링
#print(df.query(" 나이 > 50 and 기혼 == 'Married' "))   # ""안에 조건식 작성     # and는 여러 조건을 이어붙이고 싶을 떄 사용 

## 기존 list 데이터를 dataframe으로 변환가능
# ex) 셔츠 판매 데이터에 관한 리스트를 df으로
#셔츠 = [15, 20, 25]
#바지 = [150, 160, 170]

#딕셔너리 = {
#    '셔츠' : [15, 20, 25],
#    '바지' : [150, 160, 170]
#}   # 딕셔너리를 변환 시 셔츠라는 컬럼(Key)에 해당 값들이 row(value)로 들어감감

#df2 = pd.DataFrame(딕셔너리)
#print(df2)


## H.W 명제 증명해보기
# Q1. 남자고 결혼한 사람은 사용금액이 남자고 싱글인 사람에 비해 평균적으로 높을 것임?
'''
1. 남자이고 기혼 또는 미혼인 경우 필터링 후 사용금액 콜럼만 남기기기
2. 기혼인지 미혼인지를 기준으로 .groupby(mean())
'''
#df_filtered = df.query(" 성별 == 'M' and 기혼 == 'Married' or 기혼 == 'Single' ")       
    # 위와 같은 식으로 짜면 and랑 or이 동격으로 되어 여성이면서 싱글인 데이터도 출력됨
df_filtered = df.query(" 성별 == 'M' and (기혼 == 'Married' or 기혼 == 'Single') ")  # 성별 남자만 우선적으로 필터링 후 기혼여부에 따라 필터링
df_filtered = df_filtered[['성별', '기혼', '사용금액']]     # 원하는 콜럼과 해당값들만 추출하기
Ans1 =  df_filtered.groupby('기혼').mean(numeric_only=True)
print('Ans1: \n')
print(Ans1)

# Q2. 연간소득이 많을수록 사용금액이 평균적으로 높을 것임?
'''
1. 소득에 따라 사용금액 평균기반으로 카테고리화
2. 비례관계 관찰

Q.notes : 범주형으로 되어 있는 데이터와 수치형 데이터 간의 상관성분석은 어떻게?
'''
Ans2 = df.groupby('소득').mean(numeric_only=True)[['사용금액']]
    # groupby를 하면 기준이 된는 column이 인덱스로 변환된다는 점 주의하자
print('Ans2: \n')
print(Ans2)


### Pandas 3 : apply와 정규식쓰면 전처리가 편해짐
