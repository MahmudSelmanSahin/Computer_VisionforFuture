import cv2
import os

img = cv2.imread(os.path.join('.', 'data', '_.jpeg'))

resized_img = cv2.resize(img, (3924, 2208))

cropped_img = resized_img[1000:1500, 840:1420]

print(img.shape)
print(resized_img.shape)

cv2.imshow('resim', img)
cv2.imshow('boyutu degistirilmis resim', resized_img)
cv2.imshow('kirpilmis resim', cropped_img)
cv2.waitKey(0)