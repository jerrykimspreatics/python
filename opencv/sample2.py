
import cv2

img = cv2.imread('./source/strawberry.jpg', cv2.IMREAD_COLOR)

print('img.shape ', img.shape)


# height, width, channel = img.shape
height, width = img.shape[:2]

print('height ', height)
print('width ', width)
# print('channel', channel)