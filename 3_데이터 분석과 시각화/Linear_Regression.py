# ### 회귀분석 1 : 두 데이터 간의 관계 파악하는 법과 예측까지

# ## 여러 사람들의 키, 몸무게
# 키 = [170, 180, 160, 165, 158, 176, 182, 172]
# 몸무게 = [75,81,59,70,55,78,84,72] 

# import matplotlib.pyplot as plt
# #plt.scatter(키, 몸무게)
# #plt.show()      # 키가 커질수록 몸무게도 증가하는 것을 확인할 수 잇음 --> 회귀분석하면 예측도 가능

# ##  회귀분석하는 이유:
#     # 1. 데이터간 비례/반비례 여부 파악가능
#     # 2. 비례/반비례 할경우 예측 가능

# # 선이 있으면 키를 입력했을 때 몸무게 예측 가능 --> 회귀분석하고 싶으면 선을 그리기
#     # 회귀분석 선그리는 법: OLS(Ordinary Least Squares)를 충족하는 선
#         # OLS: 파란색 총 오차를 최소화시키는 선
#         # 총 오차를 구할 땐 각각의 오차들을 제곱해서 더함 ex) 오차가 +3, 오차가 -3일 때 절대값으로 표현 가능
#         # 아직 모르는 선은 수학식으로 표현 가능함 y=ax+b
#             # OLS를 만족하는 a,b를 찾으면 끝임(손수하거나 python에게 명령하여 실행 가능)

# # 파이썬 활용해서 회귀분석하는 법:
# from sklearn.linear_model import LinearRegression
# import numpy as np

# #model = LinearRegression().fit(키, 몸무게)  # 키는 x축 데이터, 몸무게는 y축데이터
#     # 선형회귀에 데이터를 넣을 때에는 array형식(1차원)으로 넣어야 함 --> numpy 활용
# 키 = np.array(키).reshape((-1,1))  # 리스트를 1차원으로 만들어주는 문법: -1은 다른 축을 기준으로 맞춰주라는 의미이므로 1차원으로 설정된 colum의 크기에 맞추어 설정된다.
# model = LinearRegression().fit(키, 몸무게)
# #print(model.score(키, 몸무게))      # R값일고 불리며 0~1 사이의 값을 가지고 1에 가까울 수록 밀접한 관련이 있음을 의미 
# #print(model.intercept_)     # y절편(b값)
# #print(model.coef_)      # 기울기(a값)
#     # 위의 기울기와 y절편을 기반으로 예측도 가능

# # 선형회귀 model 기반으로 예측하는 방법
# a = model.predict([[170]])      # 몸무게 170을 기준으로 키를 예측함
# print(a)

# plt.scatter(키, 몸무게)
# plt.plot(키, model.predict(키))    # scatter plot에 regression line그리는 방법  
# plt.show()

# ## 회귀분석 정리:
# '''
# 1. 두 데이터간의 관계 파악에 씀
# 2. OLS 알고리즘으로 선 그려서 파악가능
# 3. 선이 있다면 예측도 가능
# '''

# ### 회귀분석 2 : 변수 3개로 집값을 예측해보자

# ## 실제 데이터 기반으로 회귀분석 적용해보기

# import numpy as np
# import statsmodels.api as sm    # 대학에서 쓰는 통게분석할 때 쓰는 라이브러리

# 키 = [170, 180, 160, 165, 158, 176, 182, 172]
# 몸무게 = [75,81,59,70,55,78,84,72] 

# model = sm.OLS(몸무게, 키).fit()  # y:결과, x: 변수 -> 키(x)에 따른 몸무게(y) 
# print(model.summary())  
## Regresion Result 해석
    # R-squared: 1에 가까울수록 좋은 모델임
    # Prob (F-statistic): 가설을 세우고 증명하는 식으로 분석함  ex) 키는 몸무게와 관련이 있을 것이다?
        # ex) y = ax+b에서 a가 0것이라는 가설을 세웠을 때 그걸 확률(= 결과값)로 증명함 
            # 1.03e-08라는 결과값은 103앞에 0이 8개 붙는다는 의미 = 0.0000000103 -> 매우 낮으므로 a가 0이 아니고 즉 상관성이 있다는 의미
    # 회귀분석을 여러개 만들 수 있는데 이와 관련된 수치들도 제공해줌
        # AIC: 다른 모델과 비교해서 작을 수록 좋은 것임
    # coef는 a값
    # std err: 표준오차
    # p>|t|: 작을수록 좋음  * 0.05이하면 이 coefficient가 유의미함 <-> 0.1정도되면 coefficient가 무의미함
    # 0.025 ~ 0.975: 신뢰구간으로 95%확률로 해당구간의 최저값과 최고값인 0.390과 0.455 사이에 coefficient값이 들어갈 것임을 의미
    # 그 이하의 모델들은 직접 찾아볼 것

## 그래서 회귀분석은 데이터 두개의 관계를 찾고 싶을 때 사용

# import pandas as pd
# import numpy as np
# import statsmodels.api as sm
# df = pd.read_csv(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\california_housing.csv')      # california 집값데이터
# #print(df)
# # 지도 블록단위로 블록에 있는 모든 집의 데이터를 하나의 인덱스로 가짐 ex) rooms: 한 블록 내에 있는 모든 집들의 방 개수
#     # income: 블롥에 있는 모든 가구 income의 중앙값
#     # price: 블록에 있는 모든 가구 집값의 중앙값

# ## 위의 데이터를 기반으로 집값 예측 모델 만들어보기
# # 집값은 어떤 컬럼과 관련이 있을까?
#     # 가설: 집값 = yearx? + room? + bedroomsx?
#         # y= ax1 + bx2 + cx3
# # y값 형식: 
#     # df['price'] : 시리즈데이터로 리스트와 같은 취급을 받음
# # x값 형식:
#     # [[year1, rooms1, bedrooms1], [year2, rooms2, bedrooms2]..]와 같은 형식으로 만들어야 함
#     # 판다스로? df[['year', 'rooms', 'bedrooms']] 
# model = sm.OLS(df['price'], df[['year', 'rooms', 'bedrooms']]).fit()  # x에 3가지 값이 들어감, y = price
# #print(model.summary()) # R-squared = 0.751: 어느정도 유의미하다고 판단 가능
# ## 결과해석
#     # 3개의 독립변수에 따른 coefficient가 출력됨
#         # 각각의 p>|t|값을 통해 각 coefficient가 유의미한 지 확인할 수 있음

# ## 그럼이제 추정도 가능 --> coefficient와 intercept기반으로 식을 세운 후 대입해 직접 추정 OR predict코드작성
# a = model.predict([[20, 1000, 200]])    # 이때에도 [[a, b, c]]와 같은 형식으로 특정데이터 집어넣기
# print(a)

## 여러개 동시에검사하고 싶으면 .predict([[a, b, c], [d, e, f], ...)와 같이 작성하면 됨됨


### 회귀분석 3 : 나이로 소득을 예측해보자 (Polynomial Regression)

## 소득 분석

from scipy.optimize import curve_fit    # 곡선 추정할 때 사용하는 함수
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_table(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\income.txt')
print(df)   # income: 평균소득

## Q. 나이를 알면 소득을 추측할 수 있을까?
# 데이터 다룰 때 항상 이상치(빈칸 = NAN) 주의
    # 빈 행은 제거하거나 평균값으로 넣거나해서 해결
df = df.dropna() #하면 na인 행이 제거됨
# scatterplot으로 데이터 시각화해보기
#plt.scatter(df['age'], df['income'])    # 나이를 x축에 소득을 y축에
#plt.show()  # 분포가 linear하지 않는 경우에는 곡선을 사용하여 선을 그려야 함
    # y = 곡선 = 이차함수 = ax + bx^2 + c 

# curve_fit(함수, x축 데이터, y축데이터)
    # 함수는? : y = a*x + b*x**2 + c 수식 작성하기
def 함수(x, a, b, c):
    return a*x + b*x**2 + c     # 3차함수의 경우에는 그냥 3차함수 수식을 넣으면 됨

opt, cov = curve_fit(함수, df['age'], df['income'])     # curve_fit() 실행하면 그 자리에 데이터 2종 남음
    # cov: covariance의 약자로 = 공분산(2개의 확률변수의 선형관계를 나타내는 값)
print(opt)  # a,b,c 값을 의미(coefficients) --> y= 73x - 8x^2 -7
a,b,c = opt

## 곡선을 포함한 scatterplot 그려보기
x = list(set(df['age'].values)) # line그래프의 x축값들을 설정하기 위해 나이의 고유값들을 리스트 형식으로 추출

# Line plot을 그릴때에는 x축값에 numpy array의 형식을 사용해야 함
x = np.array(x)   # 리스트를 numpy array로 변환시켜주는 코드  *array는 리스트랑 똑같이 생겼지만 수학계산 시 행렬쓸 일이 있을 때 활용됨
plt.plot(x, 함수(x, a, b, c))   # x축에는 나이가, y축에는 직선 결과값    # 직접 함수를 넣어 설정하는 것도 가능
plt.scatter(df['age'], df['income'])    # 나이를 x축에 소득을 y축에
plt.show()