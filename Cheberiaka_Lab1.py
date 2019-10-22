# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 15:25:47 2019

@author: mcheberyaka
"""

import cv2
import numpy as np 

video = cv2.VideoCapture(0) 
a = 0
while True:
    a = a + 1
    check, frame = video.read()
    cv2.imshow("Smile!",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
showPic = cv2.imwrite("webcam_picture.jpg",frame)
print(showPic)
video.release()
cv2.destroyAllWindows     
image = cv2.imread('webcam_picture.jpg')
grayscale_image_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayscale_image_final = cv2.cvtColor(grayscale_image_original, cv2.COLOR_GRAY2BGR)
cv2.line(grayscale_image_final, (0,0), (640,480), (0, 0, 255), thickness=8, lineType=1)
cv2.rectangle(grayscale_image_final,(0,0),(146,228),(255,0,0),5) 
cv2.imshow('Before',image)
cv2.imshow('After', grayscale_image_final)
cv2.waitKey(0)
cv2.destroyAllWindows()