import numpy as np
import cv2

img = cv2.imread('data/dl1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = 176.67
s = 22.04
v = 96.08
tol = 23
hue_mod = 0.25
sat_mod = 2.15
lower_blue = np.array([(h - tol * hue_mod) / 2, 0, 0])
upper_blue = np.array([(h + tol * hue_mod) / 2, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('display', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
