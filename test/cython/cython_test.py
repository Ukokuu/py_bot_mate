import numpy as np
import pyximport

pyximport.install()

from py_bot_mate.image.image import find_pixels_with_color_tolerance
from py_bot_mate.image.image import mark_pixels_with_color
from py_bot_mate.color.color import Color
from py_bot_mate.color.finder_c import color_same_cts2
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting
import cv2
import time

img = cv2.imread('data/dl1.png')
cts = ColorToleranceSetting(Color.from_bgr(15857887), 6, 1.02, 6.30)
start = time.time()
points = find_pixels_with_color_tolerance(img, cts)
end = time.time()
print(end - start)
start = time.time()
img = np.array(mark_pixels_with_color(img, points, np.array([0, 0, 255], dtype='B')))
end = time.time()
print(end - start)
cv2.imshow('display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
