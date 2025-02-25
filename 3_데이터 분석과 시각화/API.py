### API 활용 1. 자동번역기 만들기

## 타인이 이미 만들어 놓은 자동번역기를 가져와서 사용하기 --> API 활용
    # API는 프로그램 사용법과 같은 것임
    # ex) 파파고도 API가 있어 개발자들이 가져와서 사용할 ㅜㅅ 있음
    # ex) Chat GPT도 API가 있음 --> 이를 기반으로 한 여러 AI 활용 서비스가 있음

## DeepL의 API 활용해보기   *제대로 활용하려면 카드 입력해야되기에 코드 참고용으로만 작성
    # 1. DeepL 사이트 들어가서 계정생성 및 카드 등록해서 DeepL API 키 받아오기
    # 2. DeeL 사이트에 API 사용방법이 담긴 문서가 있을 것임
    # 3. 문서에 제공된 파이썬 기반의 API활용 코드를 파이썬에 복붙하기

# 코딩애플의 DeepL API(라이브러리리) 활용 코드 
import deepl    # --> pip install deepl을 통해 deepl 라이브러리를 우선 설치해야 함
auth_key = "내 API키 넣기"

translator = deepl.Translator(auth_key)
result = translator.translate_text("Hello, world!", target_lang="FR")   # FR는 French를 의미
print(result.text) # "Bonjour, le monde !" : French로 번역해준다는 의미

# API 사용시 설치해야 하는 라이브러리가 제공되지 않는 경우도 있음
    # API 문서 페이지에 보면 HTTP Request 코드가 적혀있음 --> 파이썬으로 HTTP 요청하면 됨
# HTTP형식의 API기반으로 프로그램 가져오기
import requests
result = requests.??(??, data=??, headers=???) # result = requests.GET인지POST인지('요청할URL', data=보낼데이터, headers=헤더스) 
    # ??: 
        # 1) get인지 Post인지
        # 2) URL
        # 3) 전달할 데이터 - 딕셔너리나 리스트형식으로 기입되는 경우가 많음
        # 4) Headers정보: 전달할 부가정보 - 실제 데이터가 아닌 정보들 ex) Authorization 값
        # TIP: GPT한테 사이트에 따른 요청방식을 물어ㅗ 갠찮음
print(result.json())

## 출력된 데이터에서 원하는 데이터를 뽑아내는 법
    # ex)
        # dictionary로 시작하면: print(result.json()['translation'])
        # 그 안이 리스트면: print(result.json()['translation'][0]) 
        # 그 안이 또 dictionary: print(result.json()['translation'][0]['text']) 
