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
#df_filtered = df.query(" 성별 == 'M' and (기혼 == 'Married' or 기혼 == 'Single') ")  # 성별 남자만 우선적으로 필터링 후 기혼여부에 따라 필터링
#f_filtered = df_filtered[['성별', '기혼', '사용금액']]     # 원하는 콜럼과 해당값들만 추출하기
#Ans1 =  df_filtered.groupby('기혼').mean(numeric_only=True)
#print('Ans1: \n')
#print(Ans1)

# Q2. 연간소득이 많을수록 사용금액이 평균적으로 높을 것임?
'''
1. 소득에 따라 사용금액 평균기반으로 카테고리화
2. 비례관계 관찰

Q.notes : 범주형으로 되어 있는 데이터와 수치형 데이터 간의 상관성분석은 어떻게?
'''
#Ans2 = df.groupby('소득').mean(numeric_only=True)[['사용금액']]
    # groupby를 하면 기준이 된는 column이 인덱스로 변환된다는 점 주의하자
#print('Ans2: \n')
#print(Ans2)


### Pandas 3 : apply와 정규식쓰면 전처리가 편해짐
## 엑셀파일: 판매기록관련 장부
## 새로운 컬럼에 판매가 컬럼의 모든 값의 각각 10%를 더한 값 기록

# 라이브러리 import 및 엑셀(.xlsx파일) 오픈
import pandas as pd
raw = pd.read_excel(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\product.xlsx', engine = "openpyxl")  # (경로, 파일형식에 따른 엔진) # r''로 \이중기능 무효화
# df에서 새 컬럼 만들고 싶으면
#raw['부가세포함'] = raw['판매가'] * 1.1 # 부가세포함이라는 새로운 컬럼을 등호 오른쪽의 값을 데이터로 생성
#print(raw)

## Apply함수를 통해 컬럼데이터를 더 쉽게 조작가능
# raw['판매가'].apply(함수)   # 판매가 컬럼의 값들 하나하나에 함수를 적용시키라는 명령
    # 함수를 필요에 따라 디자인 후 입력하면 됨

def 함수(a): # a는 함수에 입력되는 숫자로 apply()에 안에서는 해당 컬럼의 값들이 a 자리에 들어가는 것
    return a*1.1

#raw['부가세포함'] = raw['판매가'].apply(함수)   # raw 데이터프레임에 새로운 컬럼으로 추가

## raw 데이터프레임을 보면 값이 없는 컬럼의 경우 그 자리에 NAN(Not A Number) 형식을 띔
    ## 상품목록에 따라 비어있는 카테고리 칼럼에 값을 지정시키는 방법?
        # 1. 상품명에 따른 카테고리 컬럼 만들기
#raw['카테고리'] = raw['상품목록'].apply(함수2)      # 기존 컬럼이 있으면 새로 지정하는 값을 덮어씀

## 글자에 어떤 단어가 있는 지 검사하고 싶으면 정규식(regex) 쓰기
import re # 필요한 라이브러리 가져오기
print(re.search('abc', 'abcdef'))     #(정규식 문법, 대상) : (이게, 여기들어있냐)
    # 결과: <re.Match object; span=(0, 3), match='abc'> : 인덱스 기준으로 어디에 포함되어 있는 지 알려줌
    # 만약에 없으면 None 뱉어줌
# 관련된 기능들
    # ^abc : abc로 시작하는 가

## if 조건문엔 온갖 자료를 넣을 수 있는데 
    # 자료에 뭔가가 있으면 True 취급급 
    # 자료가 비어있으면 False 취급

## 주의사항: pandas로 파일 읽을 떄 글자는 가끔 object로 변환됨
    # -> str(a)와 같이 string형식으로 변환
'''
# My Ans 
def 함수2(b):
    b = str(b) # int형식으로 되어 있는 이상치에는 string 포함여부를 위한 iteration과정이 아예 불가능 -> 사전에 string type으로 바꾸기
    if 'Chair' in b:
        return 'Chair'
    elif 'Table' in b:
        return 'Table'
    elif 'Mirror' in b:
        return 'Mirror'
    elif 'Sofa' in b:
        return 'Sofa'
    else:
        return 'unknown' # 항상 데이터셋에 예외나 이상치가 있는 지 확인 해야 하는 이유

raw['카테고리'] = raw['상품목록'].apply(함수2)
print(raw)
'''
