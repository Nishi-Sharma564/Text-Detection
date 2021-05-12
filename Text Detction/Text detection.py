from PIL import Image
import pytesseract
import cv2
import numpy as np


def get_string(img_path):

    im = Image.open(img_path)
    text = pytesseract.image_to_string(im)
    img = cv2.imread(img_path, 1)
    
    if(text==""):
        img = cv2.imread(img_path)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        cv2.imwrite("removed_noise.jpg", img)
        if(text==""):

            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

            cv2.imwrite("thres.jpg", img)

            text = pytesseract.image_to_string(Image.open("thres.jpg"), lang='eng')
    cv2.imshow('image',img)
    return text
        
    
    


image = input("Enter the image name")
print("--- Start recognize text from image ---")
text = get_string(image)
if(text==""):
    print("Sorry! unable to detect")
else:
    print(text)
    
    print("------ Done -------")
