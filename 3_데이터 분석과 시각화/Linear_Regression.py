### 회귀분석 1 : 두 데이터 간의 관계 파악하는 법과 예측까지

## 여러 사람들의 키, 몸무게
키 = [170, 180, 160, 165, 158, 176, 182, 172]
몸무게 = [75,81,59,70,55,78,84,72] 

import matplotlib.pyplot as plt
#plt.scatter(키, 몸무게)
#plt.show()      # 키가 커질수록 몸무게도 증가하는 것을 확인할 수 잇음 --> 회귀분석하면 예측도 가능

##  회귀분석하는 이유:
    # 1. 데이터간 비례/반비례 여부 파악가능
    # 2. 비례/반비례 할경우 예측 가능

# 선이 있으면 키를 입력했을 때 몸무게 예측 가능 --> 회귀분석하고 싶으면 선을 그리기
    # 회귀분석 선그리는 법: OLS(Ordinary Least Squares)를 충족하는 선
        # OLS: 파란색 총 오차를 최소화시키는 선
        # 총 오차를 구할 땐 각각의 오차들을 제곱해서 더함 ex) 오차가 +3, 오차가 -3일 때 절대값으로 표현 가능
        # 아직 모르는 선은 수학식으로 표현 가능함 y=ax+b
            # OLS를 만족하는 a,b를 찾으면 끝임(손수하거나 python에게 명령하여 실행 가능)

# 파이썬 활용해서 회귀분석하는 법:
from sklearn.linear_model import LinearRegression
import numpy as np

#model = LinearRegression().fit(키, 몸무게)  # 키는 x축 데이터, 몸무게는 y축데이터
    # 선형회귀에 데이터를 넣을 때에는 array형식(1차원)으로 넣어야 함 --> numpy 활용
키 = np.array(키).reshape((-1,1))  # 리스트를 1차원으로 만들어주는 문법: -1은 다른 축을 기준으로 맞춰주라는 의미이므로 1차원으로 설정된 colum의 크기에 맞추어 설정된다.
model = LinearRegression().fit(키, 몸무게)
#print(model.score(키, 몸무게))      # R값일고 불리며 0~1 사이의 값을 가지고 1에 가까울 수록 밀접한 관련이 있음을 의미 
#print(model.intercept_)     # y절편(b값)
#print(model.coef_)      # 기울기(a값)
    # 위의 기울기와 y절편을 기반으로 예측도 가능

# 선형회귀 model 기반으로 예측하는 방법
a = model.predict([[170]])      # 몸무게 170을 기준으로 키를 예측함
print(a)

plt.scatter(키, 몸무게)
plt.plot(키, model.predict(키))    # scatter plot에 regression line그리는 방법  
plt.show()

## 회귀분석 정리:
'''
1. 두 데이터간의 관계 파악에 씀
2. OLS 알고리즘으로 선 그려서 파악가능
3. 선이 있다면 예측도 가능
'''


