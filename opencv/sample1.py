import cv2

img = cv2.imread('source/strawberry.jpg')
# 이미지를 회색으로 변경
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('strawberry', img)
# 0 -> 계속 대기
cv2.waitKey(0)
cv2.destroyAllWindows()

# 파일에 쓰기
# cv2.imwrite("output/strawberry.jpg", img)
