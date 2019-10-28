import numpy as np
from sklearn.cluster import DBSCAN
import cv2
import time
from random import randrange
import pyximport

pyximport.install()

from py_bot_mate.image.image import find_pixels_with_color_tolerance
from py_bot_mate.image.image import mark_pixels_with_color
from py_bot_mate.color.color import Color
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting

img = cv2.imread('data/dl1.png')
cts = ColorToleranceSetting(Color.from_bgr(15857887), 6, 1.02, 6.30)
start = time.time()
points = find_pixels_with_color_tolerance(img, cts)
end = time.time()
print(end - start)
start = time.time()
# img = np.array(mark_pixels_with_color(img, points, np.array([0, 0, 255], dtype='B')))
end = time.time()
print(end - start)
db = DBSCAN(eps=10, min_samples=30).fit(points)
labels = db.labels_
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of clusters: %d' % n_clusters_)
for x in range(0, n_clusters_ - 1):
    indexs = np.array(np.where(labels == x)).flatten()
    img = np.array(mark_pixels_with_color(img, np.array([points[i] for i in indexs]), np.array([randrange(255), randrange(255), randrange(255)], dtype='B')))
cv2.imshow('display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
