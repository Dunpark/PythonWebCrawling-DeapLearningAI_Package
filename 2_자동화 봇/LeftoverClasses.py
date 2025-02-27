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

# ## 크롤러 방지 방법
# # 크롤러 방지기술 포함 사이트 수집해보기
# import requests
# # Amazon 아무 상품이나 검색해서 get 요청 해보기
# r = requests.get('http://amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Ddigital-text&field-keywords=monitor&crid=15KA6XVUO2VUH&sprefix=mo%2Cdigital-text%2C476')
# print(r.status_code) # 400이나 500몇이 뜨면 방어기제로 차단되었다는 의미 --> 아마존은 API를 구매해서 사용하도록 되어 있음
# print(r.content)

## 위와 같은 크롤링 보안 우회법:
# Amazon에 접속시 amazon은 이용자의 접속정보(request headers)를 알 수 있음
    # --> 이를 기반으로 거르는 것(그냥 접속하면 headers가 없거나 python으로 찍힘)
# Amazon 사이트를 브라우저에서 network탭을 들어가 확인하면 headers탭이 있는데 여기서 이용자의 접속정보를 알 수 있음
    # 이 중에서 user-agent 변수가 중요함 --> 접속기기, 브라우저 등을 알 수 있음 *만약 정보가 제대로 안 적혀 있으면 서버에서 제공 안하도록 설정해 놓은 것.
    # 파이썬에서 변수에 'user-agent' : '브라우저상의 user-agent 정보' 라는 딕셔너리 기입
    # r = requests.get('사이트 경로', headers = 변수)라는 코드를 작성해 사이트 가져오기 --> status코드가 200대가 나오면 우회성공한 것

# 코드예시 - Header 설정
'''
import requests

헤더스 = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
} # User-Agent 대문자 안되면 소문자로 해보기

r = requests.get('https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2', headers=헤더스) # headers라는 파라미터를 입력하는 것       # --> User-agent를 파이썬에서 브라우저의 요청으로 바꾼 것임
print(r.content)    # 200은 뜨지만 터미널에서 보았을 때 데이터가 안 들어있고 봇이라는 의심문구가 뜸 = 캡쳐에 걸린 것
print(r.status_code)

'''

# 2번째 (추가)우회법: 쿠키 활용하기
    # 브라우저의 application 탭에 들어가면 왼쪽 리스트 중 Cookies라는 항목이 있는데 이는 amazon이 브라우저에 몰래 저장해놓은 정보들을 의미함 = 크롤러 보안 
    # 쿠키를 그대로 복사해서 파라미터로 한번 더 추가
        # 네트워크 탭 다시 들어가서 새로고침했을 때 뜨는 파일 중 맨 처음에 뜨는 파일을 눌러
        # 아래로 스크롤하다보면 Request headers 부분에 cookie정보가 있는 것을 확인할 수 있음
        # 전체를 복사 해서 파이썬에 붙여놓고 딕셔너리의 형태로 바꾼 다음 새로운 변수에 저장하기 # 복붙했을 때 딕셔너리로 되어 있는 것들은 지우기
            # 이 과정을 해주는 기능도 찾아보면 있음
        # requests.get()의 파라미터에 추가하면 끝



# 코드예시 - Cookie 설정
'''
# ubid-main=135-239398; session-id=141293092; 어쩌구=저쩌구; ... : 브라우저에서 복붙한 cookie 형태
    # 딕셔너리와 비슷하게 만들어주기 위해서 {}로 감싸고 키랑 값 '' = '',로 구분

cookie원본 = 'ubid-main=135-239398; session-id=141293092; 어쩌구=저쩌구; ... '
cookie딕셔너리로 = {'ubid-main' = '135-239398', 'session-id' = '141293092', ... } 

r = requests.get('URL정보기입', headers = 'headers 정보기입', cookies = 'cookie 정보기입')
'''

## 에러처리: 에러나서 코드가 멈추는 것을 예방하려면
# status code를 기반으로 성공여부를 if, else로 구분 
'''
if r.status_code == 200:
    print(soup.select('.~~)[0])
else :
    print('에러났어요')
'''
# try, except 활용하기 - 에러 여부에 따라 try, else 구분
'''
try:
    print(soup.select('.~~~')[110]) # 이거를 해보고
except:
    print('안되네요;)   # 혹시 에러 뜨면 이거 해보기
'''