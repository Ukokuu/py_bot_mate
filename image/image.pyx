import cython
from py_bot_mate.color.finder_c import color_same_cts2

@cython.boundscheck(False)
cpdef unsigned char [:, :, :] find_pixels_with_color_tolerance(unsigned char [:, :, :] image, cts):
# set the variable extension types
 cdef int x, y, w, h
 # grab the image dimensions
 h = len(image)
 w = len(image[0])
 index = 0

 # loop over the image
 for x in range(0, h):
    for y in range(0, w):
        if color_same_cts2(cts, image[x, y]):
            image[x,y,2] = 255
            image[x,y,1] = 0
            image[x,y,0] = 0

 return image
