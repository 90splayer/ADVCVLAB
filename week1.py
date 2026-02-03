import cv2
import numpy as np

img = cv2.imread('surrey.png')
subimg = img[300:800, 200:550, :]
norming = img.astype(np.float32)/255.0

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('surrey', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)