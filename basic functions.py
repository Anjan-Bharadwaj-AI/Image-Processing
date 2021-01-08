import cv2
import numpy as np


kernel=np.ones((5,5),np.uint8)

#importing image

img=cv2.imread("lena.png")

# convert image to grayscale

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blur image

imgBlur=cv2.GaussianBlur(img,(7,7),0)

#canny edge detection

imgcanny=cv2.Canny(imgBlur,100,100)

# Dialatiojn of image

imgDialate=cv2.dilate(imgcanny,kernel,1)

# Eroded image

imgErode=cv2.erode(imgDialate,kernel,1)

# check the size of the image

print(img.shape)

#resize an image

imgResize=cv2.resize(img,(200,200)) #(w,h)

#crop an image

imgCrop=img[0:200,200:400] #(h,w)




#displaying image

cv2.imshow("Image",img)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
# cv2.imshow("Canny image",imgcanny)
# cv2.imshow("Dialate image",imgDialate)
# cv2.imshow("Eroded image",imgErode)
# cv2.imshow("Resized image",imgResize)
# cv2.imshow("Cropped image",imgCrop)
#

#saving imag

cv2.waitKey(0)