import cv2

'''
CascadeClassifier 객체(인스턴스)인 face_cascade는 detectMultiScale 함수를 호출하여
img_gray(회색그림)에서 얼굴을 검출한다. 검출된 얼굴은 사각형 목록으로 표시된다.
detectMultiScale 함수는 입력된 그림을 내부적으로 축소해가며 검출 대상을 검출하는 함수이다.
'''

img = cv2.imread('source/children.jpg')
# 이미지를 흑백으로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# 가중치 파일 경로
face_cascade_file = 'haarcascade_frontalface_alt.xml'
eye_cascade_file = 'haarcascade_eye.xml'

# 모델 불러오기
# CascadeClassifier - 다단계 분류기로 머신러닝 기반의 객체 검출 알고리즘 구현
face_cascade = cv2.CascadeClassifier(face_cascade_file)
eye_cascade = cv2.CascadeClassifier(eye_cascade_file)

# 객체 탐지 알고리즘 실행 - detectMultiScale()
# scaleFactor-비율만큼 반복적으로 줄여감(그림을 30% 줄여감)
# minNeighbors-최소 추가 검출 횟수로 0은 한번이라도 얼굴로 검출된 것을 모두 표시, 1은 2회 검출
faces = face_cascade.detectMultiScale(img_gray, 1.1, 5)
# roi - region of interest(관심 영역) roi_gray - 감지한 얼굴 영역의 그림
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w,y+h), (255, 0, 0), 2)
    roi_gray = img_gray[y:y+h, x:x+w]
    roi_img = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('children', img)
cv2.waitKey(0)
cv2.destroyAllWindows()