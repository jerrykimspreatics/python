import cv2
from pytesseract import pytesseract
import matplotlib.pyplot as plt

img = cv2.imread("source/car1.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pytesseract.tesseract_cmd = r"C:/Users/kiyon/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
text = pytesseract.image_to_string(img_gray, lang="kor")
print(text)

plt.imshow(img_gray, cmap='gray')
plt.show()