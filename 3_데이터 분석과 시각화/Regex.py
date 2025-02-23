### 정규식 자주 쓰는 것들만 핵심 정리

## 정규식을 잘 활용하면 데이터 전처리에 유리
## 정규식: 문자를 검사하는 식

# re.search 복습
import re
re.search('정규식', '안녕하세요') # re.search('이글자가', '여기있냐') - 있으면 obejct, 없으면 None 출력

# re.findll('이글자가','여기있냐') - 있으면 전부 [list]에 담아주
#a = re.findall('a', 'abcadefg')
#print(a)

# ^__: 시작문자
# __$: 끝나는 문자
# 특수문자 찾으려면 백슬래시 포함해서 작성 ex) re.findall('\$', '')
        # 특수문자 종류: $()[]{}*+.?\^-,        

# 이거 or 저거 찾으려면: [이거저거]
#a = re.findall('[abc]', 'abcade$fg') # abc 각각 이 포함되어 있는가
#print(a)
    # a-z를 통해 알파벳의 범위에 따라 글자들의 포함여부를 확인할 수 있음

#a = re.findall('[a-z]', 'abcade$fg') # 대문자도 가능 A-Z # 가-힣(한글에서는 힣가 마지막 글자임)도 가능

a = re.findall('[가-힣]', 'adsf안녕하세요ㅋㅋㅋ')    # 가-힣(한글에서는 힣가 마지막 글자임)도 가능

a = re.findall('[ㄱ-ㅎ]', 'adsf안녕하세요ㅋㅋㅋ')    # ㄱ-ㅎ을 통해 자음 포함여부 확인 가능

a = re.findall('[^가-힣]', 'abc안녕하세요ㅋㅋ') # 대괄호 안에 ^를 쓰면 not이라는 의미

a = re.findall('\d', 'abc안녕하세요ㅋㅋ123') # \d는 숫자가 포함되어 있는 지를 의미

# \d\d는 두자리 숫자(연속된)를 찾아줌

# \d\d\d는 세자리
    # 정규식은 순차적으로 가기에 4자리수가 있으면 앞의 3자리수를 출력하고 지운 후 남은 데이터를 기반으로 작동
    # =  4자리수가 있으면 3자리수와 한자리수로 인식함

# \d{3}은 곱셈기호로 \d 3개 = 3자리수를 의미

# \D는 숫자가 아닌것을 출력

# \s는 스페이스바를 출력함

# \S는 스페이스바가 아닌 모든 것 = 모든 문자    

a = re.findall('ㅋ+', 'abcd$f^g3545 ㅋㅋㅋ안녕하세요123')    # +는 반복해서 찾으라고 시킬 때    *단일한 대상은 무시고 연속된대상은 하나로 리스트에 추가   = greedy하게 찾는다고 표현하기도 함

a = re.findall('abc', 'abcdABC$f^g3545 ㅋㅋㅋ안녕하세요123', re.IGNORECASE)    # re.IGNORECASE 대문자와 소문자 구분없이 찾는 방법

# 특정 문자를 모두 찾아서 다른 문자로 바꾸라고 명령
a = re.sub('\-', '.', '2022-1-1')    # re.sub('이걸 찾아서', '이걸로바꿔주셈', '문장')
print(a)

# 특정 문자를 제거하려면? '': 공백으로 change
a = re.sub('\d', '', 'AVDCSD@3413')  # 숫자만 제거
a = re.sub('\D', '', 'AVDCSD@3413')  # 숫자빼고 다 제거
a = re.sub('[^\d]', '', 'AVDCSD@3413')  # 숫자빼고 다 제거
print(a) 


### H.W 

# Q1. 이메일형식이 맞는지 판단하는 정규식을 만들어보십시오. 

# Correct Ans
결과 = re.findall('\S+@\S+\.\S+', 'abc@example.com')    # 여러개의 조건을 잡을 때에는 그냥 ''안에 이어쓰면됨됨
print(f'A1 : {결과}')


# Q2. 상품목록에 Mirror 또는 Sofa라는 영단어가 포함되어있으면 카테고리컬럼에 '가구'라고 기록하고 싶습니다. 
import pandas as pd
raw = pd.read_excel(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\product.xlsx', engine = "openpyxl")  # (경로, 파일형식에 따른 엔진) # r''로 \이중기능 무효화
print(raw)

def 함수(a):
  if re.search('Mirror|Sofa', str(a)) :
    return '가구'
raw['카테고리'] = raw['상품목록'].apply(함수)
print(raw)

# Q3. 상품목록에 글자가 없고 숫자만 있으면 그 칸은 '에러'라는 단어로 바꾸고 싶습니다.
    # 숫자만 있다 = 문자가 없다

# My ANs
raw = pd.read_excel(r'D:\2025\일\개강전\개강전까지의 코딩공부\코딩애플_파이썬웹크롤러&딥러닝AI_패키지\3_데이터 분석과 시각화\product.xlsx', engine = "openpyxl")  # (경로, 파일형식에 따른 엔진) # r''로 \이중기능 무효화
print(raw)

def 함수2(b):   # re함수도 대상을 string으로 바궈야 적용가능
  if re.findall('[a-z]', str(b)): # []를 씌어줘야 a-z까지의 글자 하나하나가 포함되어 있는 지 확인한다는 의미임
    return b
  else:
    return 'error'
  
raw['상품목록'] = raw['상품목록'].apply(함수2)
print(raw)

# Corret Ans
def 함수(a):
  if re.search('\D', str(a)) :
    return a
  else :
    return '에러'
raw['카테고리'] = raw['카테고리'].apply(함수)