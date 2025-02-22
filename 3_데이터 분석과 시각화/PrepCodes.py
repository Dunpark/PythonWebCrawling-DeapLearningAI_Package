# ### 이미지 100만개를 한번에 리사이즈하고 용량압축 하려면(파이썬으로 웹서버 만들 때 필요 )

# # 터미널에 pip install Pillow를 작성해 필요한 라이브러리 설치 후 import
# from PIL import Image
# img = Image.open('images/photo1.jpg') # Image폴더의 이미지 1개 열어보기
# img = img.resize((300, 500)) # 이미지 리사이즈 하는법: .resize((가로,세로))
# img.save('new_photo1.jpg') # 새로운 이름으로 변형된 이미지가 생성 됨 
#     # 리사이즈와 동시에 비율을 유지하고 싶을 때 - .thumbnail((가로, 세로)) - 정확히는 이미지 축소
# img = Image.open('images/photo1.jpg') # Image폴더의 이미지 1개 열어보기
# img.thumbnail((300, 500)) # 주의: resize와 달리 굳이 새 변수 지정을 안해도 갠찮음
# img.save('new_photo1.jpg', quality = 65)    # quality 파라미터(0~95): 키울 수록 고화질, 줄일수록 저화질 *75가 default
#     # 만약 이미지가 png파일이면 저장 시 quantize옵션 찾아보기
# # png -> jpg 변환도 가능: png 오픈 후 jpg로 저장하면 자동변환됨
# # jpg -> progressive JPG(웹상에서 쓰는 타입으로 로딩시간이 좀 더 빠름)로 만드는 것도 가능
#     # img.save('새로 저장할 파일 이름', progressive = True) # 파라미터 활용
# #  이미지 자르는 것도 가능:
# #  흑백 변환도 가능: 
# img = Image.open('images/photo1.jpg').convert('L') # .convert('L') # 흑백변환됨
# img = img.crop( (50,50, 150, 150) ) # .crop((좌표1, 좌표2)) # 첫번째 좌표와 두번째 좌표를 대각선의 꼭짓점으로 하는 네모 구간을 기준으로 사진으로 자름 *좌표는 왼위 꼭짓점을 기준으로 함
#     # 이미지의 비율과 관련된 수학식을 세워 좌표설정도 가능
# img.save('new_photo1.jpg', quality = 65)    # quality 파라미터(0~95): 키울 수록 고화질, 줄일수록 저화질 *75가 default

# 대량으로 imgaes 폴더 내의 많은 이미지를 한번에 리사이즈 하는 법?
    # 파일들의 이름이 규칙적인 경우
        # -> 반복문으로 바꾸고 이미지 파일명의 숫자를 i로 놓아 변경
    # 파일 이름들이 불규칙적인 경우
        # 파일명딀을 []list에 담고 그걸로 for 돌림

# import os # 모든 이미지들을 하나의 파일에 담기 위해
# 경로 = os.getcwd() # 현재 다이렉토리의 절대경로
# 파일명들 = os.listdir(경로+'/images') # 합성경로의 폴더 안의 모든 파일명이 리스트에 담겨짐

# for i in 파일명들: 
#     img = Image.open('images/' + i) # images 폴더내의 파일명에 따라 for loop이 불러들임
#     img.thumbnail((500, 2500)) # 이미지의 원래 크기보다 가로,세로 값이 크면 적용이 안됨
#     img.save('new_' + i) # 규칙적인 이름으로 새로 정의함


### 파이썬으로 이메일 알림 보내는 법(SMTP)
## Why? 크롤러 만들었는데 시간이 오래 걸리는 경우
    # 완료를 알려주거나
    # 결과파일을 전송하거나
        # 그럴 때 이메일 보내라고 하면 화면보며 기다릴 필요 X

## 메일을 주고받을 땐 SMTP에 따라 주고 받음 = 통신규약(정해진 문법 같은)
# SMTP 서버를 직접 만들어야 함. ex) Naver SMTP server에서 Google SMTP server로 보내는 것과 같은 격
    # 대부분의 메일 서비스 가입하면 SMTP 서버를 원격으로 이용할 수 있는 권한 제공 

## 네이버 서버 빌려서 네이버 메일 전송하는 법
'''
import smtplib
from email.mime.text import MIMEText
 
text = "메일 내용입니다"
msg = MIMEText(text) 
 
msg['Subject'] ="test"     # "메일제목"
msg['From'] = 'chiwon0725@naver.com'    # '보내는사람이메일' 
msg['To'] = '박지원'    # '받는사람이름이나 이메일' 
print(msg.as_string()) 
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
    # 네이버 메일 환경설정에서 IMAP/SMPT에 사용함 체크 후 하단에 SMTP 서버명, 포트번호 복붙 
        # 네이버mtp주소 = smtp.naver.com
        # 포트번호 = 587
    # Gmail SMTP 주소/포트 적으면 GMAIL 빌려서 메일보내기도 가능

s.starttls() #TLS 보안 처리 - *보안 연결(TLS) 필요라고 웹에 써져 있는 경우 보안 필요 
s.login('chiwon0725', 'jordanp0725')  #( '네이버아이디' , '비번' ) #네이버로그인
s.sendmail('chiwon0725@naver.com', 'chiwon0725@naver.com', msg.as_string())     # ( '발송자이메일', '수신자이메일', msg.as_string() )  
s.close()
''' # 2차인증 안돼서 실패함

### Gmail 서버 빌려서 전송해보기
import smtplib
from email.mime.text import MIMEText
 
text = "메일 내용입니다"
msg = MIMEText(text) 
 
msg['Subject'] ="이것은 메일제목"
msg['From'] = 'chiwon0725@gmail.com'
msg['To'] = '박지원'
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.gmail.com' , 587 ) 
s.starttls() #TLS 보안 처리
s.login( 'chiwon0725', 'odvy zzxr ijvi keiz' ) #gmail로 로그인
    # 로그인을 위해 몇가지 사전 절차가 필요한데:
        # 1. 구글 계정에 들어가서 2차 확인 허용 설정하기
        # 2. app password에 들어가 password 발급 받기 *한번 발급가능하고 이후로 확인 불가능함(위의 코드 참고) But 언제든 새로 발급 가능

s.sendmail( 'chiwon0725@gmail.com', 'chiwon0725@gmail.com', msg.as_string() )
s.close()

## 메일내용에 html 작성해서 추가하는 법
# 위의 msg = MIMEText(text) 대신에 아래의 코드 넣으면 됨
'''
msg = MIMEMultipart('alternative')
내용 = """
여기에 HTML로 작성가능  ex) <h4>굵은제목</h4>
"""
part1 = MIMEText(내용, "html")
msg.attach(part1)
'''

## 메일내용에 첨부파일 추가하는 법
# msg = MIMEMultipart() 로 설정
# msg.attach(MIMEText(text))로 text변수에 있는 메일 내용도 추가하기
# 원하는 파일 rb로 오픈
'''
with open('보낼파일경로', 'rb') as 파일:
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(파일.read())

#파일 base64 인코딩
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"')
msg.attach(part)
'''