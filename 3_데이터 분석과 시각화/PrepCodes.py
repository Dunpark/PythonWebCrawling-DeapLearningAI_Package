# ### 이미지 100만개를 한번에 리사이즈하고 용량압축 하려면(파이썬으로 웹서버 만들 때 필요 )

# # 터미널에 pip install Pillow를 작성해 필요한 라이브러리 설치 후 import
from PIL import Image
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

import os # 모든 이미지들을 하나의 파일에 담기 위해
경로 = os.getcwd() # 현재 다이렉토리의 절대경로
파일명들 = os.listdir(경로+'/images') # 합성경로의 폴더 안의 모든 파일명이 리스트에 담겨짐

for i in 파일명들: 
    img = Image.open('images/' + i) # images 폴더내의 파일명에 따라 for loop이 불러들임
    img.thumbnail((500, 2500)) # 이미지의 원래 크기보다 가로,세로 값이 크면 적용이 안됨
    img.save('new_' + i) # 규칙적인 이름으로 새로 정의함


### 파이썬으로 이메일 알림 보내는 법(SMTP)

