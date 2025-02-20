### 파일 100만개 손수 조작하기 귀찮으면 os module 사용

## 파일 백만개 rename하기, 분류하기 등등 많이 활용됨

## 파이썬으로 PC파일 조작

import os 
파일들 = os.listdir('test') # 테스트 폴더에 있는 모든 파일 가져오기
print(파일들)
