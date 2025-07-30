# AntiCaptcha
# Application Coded By  Nima Zare  www.nimazare.org

import cv2
import pytesseract
import re

def Convert(list_chars):
    new = ""
    for x in list_chars:
        new += x

    return new 


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread(r"C:\Users\Programmer\Desktop\filtered.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# # Morph open to remove noise and invert image
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# invert = 255 - thresh
# Perform text extraction
data = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
print("\n\n--------------Process Data--------------")
print(f"data: {data}")
print("----------------------------")
chars_list = re.findall("[a-zA-Z0-9]", data)
nima = Convert(chars_list)
if nima == "" or len(nima) <= 6:
    print('Empty String !')
    exit()

revers = nima[::-1]
print(nima)
print("----------------------------")
print(f"Reversed : {revers}")
print("----------------------------")
print(f"Final Answer : {nima[0:3]}{nima[3]}{nima[0:3]}")
print("----------------------------")
print(F"Final Revers : {revers[2]}{revers[1]}{revers[0]}{revers[3]}{revers[2]}{revers[1]}{revers[0]}")
print("-------------End---------------")
# cv2.imshow('thresh', thresh)
# cv2.imwrite(r"C:\Users\Programmer\Pictures\Test\image2.png", thresh)
# cv2.imshow(f'{nima}', invert)
# cv2.imwrite(r"C:\Users\Programmer\Pictures\Test\image3.png", invert)
cv2.waitKey()
