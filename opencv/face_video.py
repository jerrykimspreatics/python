import cv2

# 영상 파일
cam = cv2.VideoCapture('sample.mp4')
# 사진 파일
img = cv2.imread('sample.jpg')


# 영상 재생
def videoDetector(cam, cascade):
    while True:
        # 캡처 이미지 불러오기
        ret, img = cam.read()
        # 영상 압축
        img = cv2.resize(img, dsize=None, fx=0.75, fy=0.75)
        # 그레이 스케일 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 사진 출력
def imgDetector(img, cascade):
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)