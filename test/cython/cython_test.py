import numpy as np
import pyximport

pyximport.install()

from py_bot_mate.image.image import find_pixels_with_color_tolerance
from py_bot_mate.color.color import Color
from py_bot_mate.color.finder_c import color_same_cts2
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting
import cv2
import time

img = cv2.imread('data/dl1.png')
cts = ColorToleranceSetting(Color.from_bgr(15857887), 6, 1.02, 6.30)
start = time.time()
img = np.array(find_pixels_with_color_tolerance(img, cts))
print(img[0])
end = time.time()
cv2.imshow('display', img)
print(end - start)
cv2.waitKey(0)
cv2.destroyAllWindows()
