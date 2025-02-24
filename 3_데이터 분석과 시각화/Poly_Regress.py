### Statsmodels로 진행하는 Polynomial Regression, 그리고 overfitting

import statsmodels.api as sm
import numpy as np
import pandas as pd

df = pd.read_table(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\income.txt')
df = df.dropna()
print(df)
x = np.column_stack([df['age'], df['age']**2, np.ones(79)]) # np.ones(78) : 1이 78개 들어 있다는 의미
    # [[첫항목들],[둘째항목들], [셋째항목들]..]과 같은 식으로 리스트에 담김
model = sm.OLS(df['income'], x).fit()  # y=ax + bx^2 + c  # x = [[첫놈나이, 첫놈나이^2, 상수]], y = []
print(model.summary())
## 결과해석
    # const(상수항)의 P>|t| 값이 거의 0.5에 가까운 것을 확인할 수 있음
        # -> 확률이 좀 높으면 쓸데없는 변수일 수 있음 --> 상수 제거하는 게 오히려 정확도를 올릴 수도 있음
            # 상수O: 0.994 -> 상수X: 0.793

# Overfitting 현상: 모델의 차수를 너무 많이 올리면 overfitting(과적합현상)이 일어날 수도 있음 
    # 학습데이터셋에 너무 적합해져 다른 상황에 응용할 수 없는 수준이 될 때
