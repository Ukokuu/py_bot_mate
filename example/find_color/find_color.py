import numpy as np
import cv2
from py_bot_mate.color.color import Color
from py_bot_mate.color.finder import Finder
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting
import time

img = cv2.imread('data/dl1.png')
mark_color = Color(0, 0, 255).to_array()
cts = ColorToleranceSetting(Color.from_bgr(15857887), 6, 1.02, 6.30)
start = time.time()
for i in range(len(img)):
    for j in range(len(img[0])):
        if Finder.color_same_cts2(cts, img[i][j]):
            img[i][j] = mark_color
end = time.time()
cv2.imshow('display', img)
print(end - start)
cv2.waitKey(0)
cv2.destroyAllWindows()
