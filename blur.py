import cv2
import os

img = cv2.imread(os.path.join('.','data','sadas.jpeg'))

k_size = 22
blurred_img = cv2.blur(img, (k_size, k_size))

cv2.imshow('blurred_img', blurred_img)
cv2.imshow('img', img)
cv2.waitKey(0)