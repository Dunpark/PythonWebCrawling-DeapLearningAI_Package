### Langchain 1. LLM 활용과 LCEL
## Langchain: OpenAI와 같은 API 요청을 쉽게 해주는 라이브러리   * 이 경우에도 사전에 터미널에 API 키 등록하는 과정이 우선되어야 함
    # 웹크롤링도 쉽게 하게 해주는 기능 있음
    # DB 유사도검색
    # AI 답변 변형
    # AI 답변 기억 구현 능력
    # API 병렬처리
    # "agent" 사용가능 : AI가 직접 자료수집등 사람과 같이 일처리를 할 수 있게 해줌 but 성능 bad
# 나중에 코딩할 떄 문서참고가능 + 협업 시 편리하기에 자주 사용됨

## Langchain 써서 API 요청하기 **** pydantic이 현재는 2.10.6버전까지 있는데 해당 라이브러리는 1.10.11을 활용 = 오래된 기능일 가능성 높음 --> 참고용으로 
    # pip install langchain_openai langchain_core로 필요한 라이브러리 설치
        # 만약 파일 실행시 pydantic 어쩌구 에러나면 --> pip install pydantic==1.10.11 터미널에 실행하기

from langchain_openai import ChatOpenAI
import os # API 키 인터페이스에서 등록하는 법
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser   # 출력결과를 string으로 바꾸기 위한 클래스스
from langchain_core.output_parsers import SimpleJsonOutputParser

'''
os.evnrion["OPENAI_API_KEY"] = '본인 api 키'    # 이 코드를 통해 터미널에 API키 등록하는 과정 대체가능

model = ChatOpenAI(model = 'gpt-40-mini')   

template = ChatPromptTemplate.from_messages(    # 이런식으로 메시지를 기반으로 템플릿을 만들면 메시지의 일부분에 구멍 뚫어넣고 템플릿 상황에 맞게 재활용가능
    [
    ('system', '너는 지금부터 영어를 한글로 번역해주는 봇임'),
    ('human', 'I love programming')
    ]
)

msg = [
    ('system', '너는 지금부터 영어를 한글로 번역해주는 봇임'),
    ('human', 'I love programming')
]

result = model.invoke(template.format_messages(구멍='I like kimchi'))  # # OpenAI API 요청이 됨
print(result.content)   

## 함수를 대신해서 사용가능 한 LCEL 문법이 LanngChain에 포함됨  = Pipe 문법: 직관적으로 뭐가 어디 들어가는 지 볼 수 있음
result = (데이터 | template | model).invoke({'구멍' : 'I like kimchi'})    # 왼쪽에서 나온 결과(template에 )를 오른쪽에 집어넣으라는 의미로     # 데이터를 template에 넣는 것도 가능
print(result.content)

# ex) dictionary 형태로 출력결과를 parse하려면?
result = (데이터 | template | model | StrOutputParser()).invoke({'구멍' : 'I like kimchi'})
    # string형식으로 출력해줌
result = (데이터 | template | model | SimpleJsonOutputParser()).invoke({'구멍' : 'I like kimchi'})
    # 딕셔너리 형태로 출력해줌
'''

### Langchain 2. RAG로 AI답변 정확도 높이기

## LLM의 Hallucination: AI가 알지 못하는 내용에 대해서 그럴듯하게 틀린 내용을 제공
    # LLM은 문자 자동완성 AI로 전문분야에서 쌩으로 활용하기 어려움
# --> 데이터를 먼저 AI에게 제공하고 이를 참고해서 답변하라고 함 = RAG(Retrieval Augmented Generation)
    # ex) 비슷한 내용을 게웹에서 검색해오고 그걸 참고 해서 AI에게 답변하라고 시키기.

# 데이터 수집해서 프롬프트에 넣어보자
    # 웹페이지 수집해서 넣어보기
from langchain_community.document_loaders import WebBaseLoader  # 먼저 pip install langchain langchain_community
from langchain.chains.summarize import load_summarize_chain  # gpa에게 요청하여 자동으로 요약 요청함
model = ChatOpenAI(model='gpt-40-mini') # 요약해주는 모델의 종류 설정

loader = WebBaseLoader('https://news.naver.com')
docs = loader.load()
print(docs) # 출력결과에서 \n은 줄바꿈을 의미

# 출력결과를 편하게 요약하고 싶으면
''' ***API키 필요   
chain = load_summarize_chain(model, chain_type='stuff') # API 요청해서 요약본 제공해줌
result = chain.invoke(docs)
print(result)
'''

# PDF내용 쉽게 불러오려면
'''
from langchain_community.document_loaders import PyPDFLoader
pdf = PyPDFLoader(('~~')).load()
'''

# DB에서 데이터가져오기
    # 사용하는 DB사용법에 따라 원하는 거 검색 해오기
    # embedding으로 유사도검색해서 가져오는 경우도 있음
        # 문자를 학습할 때에는 숫자들로 구성된 리스트 형식으로 바꾸어서 넣는데 이때 이것을 embedding이라고 부름
        # 요즘 변환해주는 API도 있음
        # 요즘 embedding은 유사문장 검색에도 사용함 --> embedding값이 비슷하기 때문에 글 자체로도 유사하다는 결론을 낼 수 있음
        # embedding은 벡터와도 같기 때문에 cosine 유사도를 기반으로 거리를 확인 하면 유사도를 확인할 수 있음
            # --> embedding 저장을 위한 vector 데이터베이스가 유행임

## Rag 구현해보기 - SAM2라는 모델 설치법 AI한테 물어보기
    # 설치법이 있는 웹페이지 내용을 AI에게 주고 명령 실행
model = ChatOpenAI(model='gpt-40-mini') # 요약해주는 모델의 종류 설정

loader = WebBaseLoader('http://github.com/facebookresearch/segment-anything-2')
docs = loader.load()

template = ChatPromptTemplate.from_template("""
    질문에 대해서 context부분을 읽고 답변을 작성해줘:
    context: {context}  # 웹페이지 내용
    질문: {question}
    답변:
""")   # 문자만 집어넣을 수 있으며 이를 통해 AI에게 바로 질문가능

chain = template | model | StrOutputParser()    # 결과를 string형식으로 출력

result = chain.invoke({'context': docs, 'question' : 'SAM2 모델 설치는 어떻게 해야 함?'})
print(result)



    