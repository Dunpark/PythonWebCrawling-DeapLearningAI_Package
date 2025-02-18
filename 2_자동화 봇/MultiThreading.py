### 파이썬 멀티쓰레딩 1: 수집할 페이지가 백만개 있으면 어쩌죠

import requests
import json
import time


# 코인원의 ETH 코인가겨이고 JSON으로 올 것임
url = [
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

# URL에 들어있는 데이터를 가져오는 크롤러 생성 코드
data = requests.get('~~') # 첫번쨰 URL
딕셔너리 = json.loads(data.content)
print(딕셔너러ㅣ['data'][0]['Close'])
# 근데 만약 URL이 여러개면 가져오는 데 시간이 오래 걸릴 것이고 for루프를 사용한다 해도 코드하나하나 순차적으로 진행하기에 시간소모 too much
## multi - processing / multi - threading을 활용해 병렬 작업시키면 해결가능

def 함수(): # 함수를 사용하면 200 개의 데이터 콘텐츠 중 첫번째를 가져옴
    data = requests.get('~~') # 첫번쨰 URL
    딕셔너리 = json.loads(data.content)
    return 딕셔너러ㅣ['data'][0]['Close']

함수( url[0] )
함수( url[1] )
함수( url[2] )
# 함수에 url을 각각 넣어 필요한 데이터 추출


## multi-processing : 여러개의 파이썬 실행창 띄우기
## multi-threading: CPU 병렬처리
    # 코드 짜기 어려움
    # 원하는 데로 동작하지 않을 가능성 유
        # 변수를 변경하고 싶을 때 변수에 lock이 걸려 다른 변수들은 수정하지 못하게 함
        # --> 여러개의 변수를 한 번에 변경하지 못함. --> 병목현상 발생 

## 멀티쓰레딩으로 코드실행시키는 법
from multiprocessing.dummy import Pool as ThreadPool # Pool함수를 ThreadPool이라는 이름으로 사용 # .dummy를 붙이면 multi processing이 아닌 multi threading을 활용한다는 의미

pool = ThreadPool(4) # 4개의 작업을 동시에 병렬처리 한다는 의미
pool.map() 
pool.close()
pool.join()






