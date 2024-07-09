import cv2

'''
과거 얼굴인식은 첩보영화나 CSI와 같은 드라마에서 범죄자를 찾는데 활용되는 신기술로 인식되었으나, 
머신러닝과 하드웨어의 발전으로 이젠 일상에서 쉽게 접할 수 있게 되었습니다. 
현재 얼굴인식 기술은 크게 탐지(Detection)과 인식(Identification)으로 나뉘고 있습니다. 
페이스북이나 인스타그램에 사진을 업로드할때 얼굴을 찾아주는 탐지 기술, 아이폰 보안 기술로 
활용되는 Face ID는 인식 기술이 대표적이고 우리에게 친숙한 얼굴 인식 응용 기술이다.

OpenCV에서 기본 라이브러리로 제공하는 Haar Cascade는 기계학습을 이용한 객체 탐지 알고리즘입니다. 
CNN이나 RSTM 등의 신경망이 아닌, 하르 특징 (Haar Features) 계산을 통해 객체를 찾습니다. 
사전 학습된 분류기 (haarcascade_frontalface_alt.xml) 를 로드한 뒤, 
cv2를 통해 분류기를 생성해줍니다.

CascadeClassifier 객체(인스턴스)인 face_cascade는 detectMultiScale 함수를 호출하여
img_gray(회색그림)에서 얼굴을 검출한다. 검출된 얼굴은 사각형 목록으로 표시된다.
detectMultiScale 함수는 입력된 그림을 내부적으로 축소해가며 검출 대상을 검출하는 함수이다.
'''

img = cv2.imread('source/children.jpg')
# 이미지를 흑백으로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# 가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_alt.xml'

# 모델 불러오기
# CascadeClassifier - 다단계 분류기로 머신러닝 기반의 객체 검출 알고리즘 구현
face_cascade = cv2.CascadeClassifier(cascade_filename)

# 객체 탐지 알고리즘 실행 - detectMultiScale()
# scaleFactor-비율만큼 반복적으로 줄여감(그림을 30% 줄여감)
# minNeighbors-최소 추가 검출 횟수로 0은 한번이라도 얼굴로 검출된 것을 모두 표시, 1은 2회 검출
faces = face_cascade.detectMultiScale(img_gray, 1.3, 4)
# 좌표 - x, y 크기 - w, h 색상 두께
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w,y+h), (255, 0, 0), 2)

cv2.imshow('children', img)
cv2.waitKey(0)
cv2.destroyAllWindows()