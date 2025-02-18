### time과 관련된 여러 문법
import time

## 현재 시간 출력
print(time.time()) # epoch time이 출력됨 *1970년을 시작으로 몇초가 흘렀는지 보여줌

a = time.time()
# 처리시간이 오래 걸리는 코드가 있으면 코드를 시행 후의 시간은 다르게 출력될 것임
b = time.time()
print(b-a) # 코드가 시행되는데 걸리는 시간 확인 가능

## 현재 ctime을 출력하는 법 - 사람이 보는 시간
시간 = time.time() 
시간 = time.ctime(시간) # 사람이 읽을 수 있는 현재시간으로 변환
print(시간)
# 필요한 일부 시간만을 출력하는 법
시간 = time.localtime() 
print(시간) # time.struct_time()은 시간의 요소들을 정리해 놓은 것과 같다고 보면 됨
print(시간.tm_hour) # 요소를 직접 입력해 필요한 요소만을 부를 수 있음  # .뒤에 control + space bar를 누르면 시간 요소들 목록이 뜸
# strftime()으로 시간표시형식 맘대로 바꾸기
시간 = time.localtime()
a = time.strftime('%Y year %m month', 시간) # year와 month를 string으로 추가하여 출력 *한국어는 인식못함 : strftime('포맷팅문법', timelocaltime())
print(a) # 년월일 시분초 활용가능

# 시간 쉽게 출력하는 방법
import datetime
a = datetime.datetime(2022, 10, 1, 12, 12, 30) # 2022년 10월 1일 12시 12분 30초
print(a)

