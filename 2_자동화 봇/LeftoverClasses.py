# ### 파일 100만개 손수 조작하기 귀찮으면 os module 사용

# ## 파일 백만개 rename하기, 분류하기 등등 많이 활용됨

# ## 파이썬으로 PC파일 조작
# import os 
# 파일들 = os.listdir('test') # 테스트 폴더에 있는 모든 파일 가져오기
# #print(파일들)

# # 파이썬으로 파일명 변경
# #os.rename('test/1.txt', 'test/4.txt') # test파일 안에 있으니까   # A -> B # 원하는 경로에 있는 파일명의 이름을 바꿀 수 있음

#     # 변경할 파일명이 여러개일 경우?
# for i in os.listdir('test'): # 테스트 폴더 안의 모든 파이령을 리스트로 가져와주세요 --> i는 각 파일명 
#     os.rename(f'test/{i}', f'test/a{i}') # 모든 파일이 동일한 방식으로 이름이 변경됨

# # 파이썬으로 파일 복사하기

# import shutil # 파일 복사하는 데에 필요한 라이브러리

# # shutil.copy('파일명', '파일명') # A -> B # 경로로 파일이 복사됨
# for i in os.listdir('test'):
#     shutil.copy(f'test/{i}', f'test2/{i}')

# ## 조건에 맞는 것만 복사
# # for i in os.listdir('test'):
# #     if : # 만약에 지금 if라는 파일명에 jpg가 들어있으면:

# # 경로 주의점
#     # 절대 경로는 PC에서 파일의 전체경로를 의미
#     # 경로 내의 backslash는 이종기능으로 에러가 날 때가 있으므로 r'경로'와 같이 작성하는 것이 에러가능성을 없앰
#     # 같은 폴더 안에 들어 있으면 절대 경로말고 상대경로로 작성간으  
#     # 경로를 나누어 +로 구분하면 원하는 대로 특정 경로 내에서 변화를 줄 수 있음
#         # ex) os.rename( r'C:\user\harry\desktop\ + f'test\{i}') 
#     # os.path.join('경로', '경로2') # 위와 같이 경로 2개를 합쳐 줌
#     # os.getcwd(): 현재 경로를 알려주는 함수 = current working directory.
    
# import os 
# os.getcwd() # --> d:\2025\일\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지


# ### 어려워하는 class/objet 문법 세계 최고로 쉽게 설명해드림
    ## class 문법은 필수는 아니지만 비슷한 내용을 가진 object 자료를 여러개 찍어낼 때 매우 유용하게 사용가능


# ## 게임 정보제공 사이트를 만들 때
#     # 각 캐릭터의 정보를 자료형으로 정리하는 게 우선

# # nunu = {
# #     'q': 'eat', 
# #     'w':'snowball' 
# # } # 보기 편하게 줄로 구분

# # garen = {
# #     'q': 'strike', 
# #     'w':'courage'
# # }

# # 오브젝트만드는 문법
# #오브젝트.q = 'eat' # object에 자료 추가하는 방법

# # 유사한 object들을 한 줄 컷으로 생성해주는 class 문법
# # class Hero: # Hero라는 object가 생성된 것임
# #     q = 'eat'
# #     w = 'snowball'

# # 오브젝트1 = Hero() # object가 생산됨
# # 오브젝트2 = Hero() # object가 하나더 생산됨
# # print(오브젝트1.q)
# # print(오브젝트2.q) # 같은 class이므로 오브젝트1과 같은 속성을 지니고 있음

# ## 올바른 class 작성법
# # class Hero:
# #     def __init__(self):     # class에서 object뽑을 때 초기값 부여하는 법 --> object 뽑으면 자동으로 def__init__ 실행됨
# #         self.q = 'eat'  # self는 새로 생성되는 오브젝트로 instance라고 부름     # .q가 붙은 건 object에 attribute를 추가했다는 의미
# #         self.w = 'snowball'

# # nunu = Hero() # 해당 변수(nunu)를 self로 하는 오브젝트 생성
# # garen = Hero()
# # print(nunu.q) 
# # print(garen.q) 

# ### class/object 문법 더 알아야할 내용

## 다른 캐릭터들에게는 다른 attribute을 추가하는 방법
class Hero:
    def __init__(self, 구멍): # 구멍에 입력값 넣을 수 있음
        self.q = 구멍   # Hero()안의 입력값으로 직접 설정 
        self.w = 'snowball'

## class에 함수도 저장할 수 있음
    def hello(self): # self는 언제나 class로부터 새로 생성되는 object를 뜻함
        print('안녕하세요') # 출력시켜주는 함수 포함된 

nunu = Hero('eat') # object 하나 뽑는데 구멍자리에 'eat'이 들어감 -> q attriute값이 구멍의 입력값(eat)이 됨
garen = Hero('strike')
print(nunu.q)
print(garen.q)
nunu.hello() # class안의 함수 실행시키는 방법
garen.hello()

## 주의점: 만약 class를 안 쓰고 위에서 만든 dictionary 형태를 활용해 garen = nunu로 작성을 하면?
    # =는 대입 표시로 garen에 nunu가 대입되어 같은 형식을 지니게 됨
    # 하지만 복사가 아닌 대입을 통한 '값공유'이므로 nunu나 garen을 수정하면 다른 것도 동일하게 수정됨 --> 서로 영향을 미침

    # 만약 서로 영향을 미치는 것을 class로 만들고 싶으면   
        # class Hero:
        # x = 123
        # def __init__(self, 구멍):
            # 위와 같이 함수 이전에 작성한 것들은 모든 class들이 공유하며 관련된 변화들도 같이 공유함    


### Python 크롤링을 막아보자 & 뚫어봊(Amazon.com)
