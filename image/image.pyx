import cython
import numpy as np
from py_bot_mate.color.finder_c import color_same_cts2


@cython.boundscheck(False)
cpdef unsigned char[:, :, :] mark_pixels_with_color(unsigned char [:, :, :] image, unsigned int [:, :] coords, unsigned char[:] color):
    length = len(coords)
    for i in range(0, length):
        coord = coords[i]
        image[coord[1], coord[0], 0] = color[0]
        image[coord[1], coord[0], 1] = color[1]
        image[coord[1], coord[0], 2] = color[2]

    return image


@cython.boundscheck(False)
cpdef unsigned int [:, :] find_pixels_with_color_tolerance(unsigned char [:, :, :] image, cts):
    # set the variable extension types
    cdef int x, y, w, h
    # grab the image dimensions
    h = len(image)
    w = len(image[0])
    index = 0
    points = np.zeros(w * h, dtype=(np.uint32,2))

    # loop over the image
    for x in range(0, h):
        for y in range(0, w):
            if color_same_cts2(cts, image[x, y]):
                points[index, 0] = y
                points[index, 1] = x
                index += 1

    points = points[~np.all(points == 0, axis=1)]
    return points
