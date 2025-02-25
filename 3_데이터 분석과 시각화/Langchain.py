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



os.evnrion["OPENAI_API_KEY"] = '본인 api 키'    # 이 코드를 통해 터미널에 API키 등록하는 과정 대체가능

model = ChatOpenAI(model = 'gpt-40-mini')   

template = ChatPromptTemplate.from_messages(    # 이런식으로 메시지를 기반으로 템플릿을 만들면 메시지의 일부분에 구멍 뚫어넣고 템플릿 상황에 맞게 재활용가능
    [
    ('system', '너는 지금부터 영어를 한글로 번역해주는 봇임'),
    ('human', 'I love programming')
    ]
)

'''
msg = [
    ('system', '너는 지금부터 영어를 한글로 번역해주는 봇임'),
    ('human', 'I love programming')
]
'''

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


### Langchain 2. RAG로 AI답변 정확도 높이기





