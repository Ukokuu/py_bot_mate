import numpy as np
import cv2
import time
from random import randrange
import pyximport

pyximport.install()

from py_bot_mate.image.image import find_cluster_with_color_tolerance
from py_bot_mate.image.image import mark_pixels_with_color
from py_bot_mate.color.color import Color
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting

img = cv2.imread('data/dl1.png')
cts = ColorToleranceSetting(Color.from_bgr(15857887), 6, 1.02, 6.30)

start = time.time()
clusters = find_cluster_with_color_tolerance(img, cts, min_pixels=300, eps=12, min_samples=20)
end = time.time()
print(end - start)

for cluster in clusters:
    img = np.array(mark_pixels_with_color(img, np.array(cluster), np.array([randrange(255), randrange(255), randrange(
        255)], dtype='B')))

cv2.imshow('display', img)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
