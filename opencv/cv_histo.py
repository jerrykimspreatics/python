import cv2
import numpy as np

# 원본 이미지
image = cv2.imread("./source/strawberry.jpg")

# 이미지 너비와 높이 가져오기
height, width = image.shape[:2]
# 원본 이미지 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 가로 세로 32x 32 픽셀에 RGB 색상 채널이 있다면, Numpy로 [32, 32, 3]차원의 배열을 생성
# uint8 - 데이터 타입을 값이 부호가 없는(unsigned) 8비트 정수(integer)가 되어 0~255 사이의 값을 나타냄
result = np.zeros((height, 256), dtype=np.uint8)

# 히스토그램 값 - 원본 매트릭스, 채널수, 이미지마스크, 히스토그램 크기, 색상값 범위
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# 값의 범위를 정규화(최소값 0 ~ 최대값 255로 변환)
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

# 히스토그램 값을 갖고 값의 크기만큼 선이 길이를 정하고 선을 그림
for x, y in enumerate(hist):
    cv2.line(result, (x, height), (x, int(height-y[0])), 255)

# 가로로 매트릭스(배열) 붙이기(스택 구조- 열을 만듬)
dst = np.hstack([image[:, :, 0], result])
cv2.imshow("dst", dst)

# 사용자 입력이 들어오면 창을 모두 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()


