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


### API 활용 2. 디자인 생성 서비스 (GPT, Dall-e)

## GPT API 활용해보기 - 카드 등록 + 유료여서 일단 코드 참고용
# 프로그램 안에서 GPT를 활용할 수 있는 것임
# GPT 파이썬으로 가져오는 방법:
    # 1. OPENAI API 사이트로 가서 가입 및 카드등록
    # 2. API KEY 발급 메뉴 찾아서 발급하기  *API Key는 한번만 보여주기에 잃어버리면 재발급 해야 함
    # 3. pip install openai를 터미널에 돌려 필요한 라이브러리 가졍괴
    # 4. OpenAI는 API key 터미널에 등록해야 사용가능 * 터미널 새로 킬 때 마다 돌려야 함
        # 4-1: set OPENAI_API_KEY 본인API키 
        # 4-2: 만약 터미널 이름이 powershell이면 $env:OPENAI_API_KEY='본인API키' 터미널에 한번 더 돌리기
# GPT --> 다음글자 예측하는 AI임
    # GPT의 API가 제공되는 것임
        # customizing 가능
            # temperature라는 파라미터로 답변의 독창성 설정가능
            # 기본 프롬프트도 설정하기 쉬움
# ChatGPT --> GPT를 챗봇처럼 사용할 수 있게 만든 툴
# 파이썬에서 가져온 GPT 활용하는 방법 - text 생성:
    # Open API documentation에서 text generation 탭에 있는 예제 코드를 기반으로 작성해보기
    # ex)
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",  # 사용할 GPT 모델델
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},  # GPT의 역할 - ex) '너는 이제 선생님이다': 선생님의 입장에서 답변할 것임
    {"role": "user", "content": "Who won the world series in 2020?"},   # GPT에게 물을 질문을 입력하는 곳
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # 올바른 답변 샘플을 줄 수 있음 = "few shot prompting": 원하는 답변 형식이 안나올 때 쓰면 좋음음
    {"role": "user", "content": "Where was it played?"} # 질문을 하나 더 할 수도 있음
  ]
)
print(response.choices[0].message.content)  # respons

# 파이썬에서 가져온 GPT 활용하는 방법 - 이미지 생성
    # TEXT와 같이 사이트에서 예재코드 기반으로 작성하기
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3", # 모델이름
  prompt="a white siamese cat", # Tip: prompt를 얼마나 잘 쓰냐에 따라 이미지의 퀄리티가 달라짐(목적에 맞게 입력하기) ex) 실험을 통해 최적의 프롬프트를 작성하는 것이 중요하기에 모델과 목적에 적합한 프롬프트를 사고파는 마켓도 있음
  size="1024x1024", # 사이즈는 모델마다 다른데 dall-e-3같은 경우에는 총 3가지 있음(1024*1024, 1024*1792, 1792,*1024)
  quality="standard",   # hd로 바꿀 수 있지만 대신 요금이 더 나옴
  n=1,
)

image_url = response.data[0].url
print(image_url)    # 3~4개 뽑아서 원하는 그림에 가장 근접한 그림 활용하는 것이 좋음

# 출력한 이미지 다운로드 받는 방법:
import requests
data = requests.get(image_url).content
with open('이미지명.jpg', 'wb') as handler:
    handler.write(data) 
    
## 이런 GPT의 기능을 웹에 포함시켜 웹서비스를 개발하는 것이 가능함 
    # --> 위에 프롬프트가 중요하다고 한 것과 같이 특정한 테마의 이미지를 생성하는 서비스를 만들면 쓸모있음

## 생성결과 별로일때? --> stable diffusion과 같이 로컬 컴퓨터에서도 돌릴 수 있는 모델 활용해보기
