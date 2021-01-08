import cv2
import numpy as np

img = np.zeros((712, 712, 3), np.uint8)
# print(img)

#convert all image to blue

#img[:]= 255,0,0

#print a line

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255,255, 255), 3)

# add a rectangle

cv2.rectangle(img, (50, 0), (250, 350), (0, 255, 255), 3)

#add circle

cv2.circle(img, (500, 200), 100, (0, 255, 0), 5)

# add text

cv2.putText(img, " Image Processing ", (100, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 150, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)