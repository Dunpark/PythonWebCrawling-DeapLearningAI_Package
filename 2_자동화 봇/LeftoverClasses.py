### 파일 100만개 손수 조작하기 귀찮으면 os module 사용

## 파일 백만개 rename하기, 분류하기 등등 많이 활용됨

## 파이썬으로 PC파일 조작
import os 
파일들 = os.listdir('test') # 테스트 폴더에 있는 모든 파일 가져오기
#print(파일들)

# 파이썬으로 파일명 변경
#os.rename('test/1.txt', 'test/4.txt') # test파일 안에 있으니까   # A -> B # 원하는 경로에 있는 파일명의 이름을 바꿀 수 있음

    # 변경할 파일명이 여러개일 경우?
for i in os.listdir('test'): # 테스트 폴더 안의 모든 파이령을 리스트로 가져와주세요 --> i는 각 파일명 
    os.rename(f'test/{i}', f'test/a{i}') # 모든 파일이 동일한 방식으로 이름이 변경됨

# 파이썬으로 파일 복사하기

import shutil # 파일 복사하는 데에 필요한 라이브러리

# shutil.copy('파일명', '파일명') # A -> B # 경로로 파일이 복사됨
for i in os.listdir('test'):
    shutil.copy(f'test/{i}', f'test2/{i}')

## 조건에 맞는 것만 복사
# for i in os.listdir('test'):
#     if : # 만약에 지금 if라는 파일명에 jpg가 들어있으면:

# 경로 주의점
    # 절대 경로는 PC에서 파일의 전체경로를 의미
    # 경로 내의 backslash는 이종기능으로 에러가 날 때가 있으므로 r'경로'와 같이 작성하는 것이 에러가능성을 없앰
    # 같은 폴더 안에 들어 있으면 절대 경로말고 상대경로로 작성간으  
    # 경로를 나누어 +로 구분하면 원하는 대로 특정 경로 내에서 변화를 줄 수 있음
        # ex) os.rename( r'C:\user\harry\desktop\ + f'test\{i}') 
    # os.path.join('경로', '경로2') # 위와 같이 경로 2개를 합쳐 줌
    # os.getcwd(): 현재 경로를 알려주는 함수 = current working directory.
    
import os 
os.getcwd() # --> d:\2025\일\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지


### 어려워하는 class/objet 문법 세계 최고로 쉽게 설명해드림