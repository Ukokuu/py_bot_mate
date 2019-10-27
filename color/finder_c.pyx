import cython

@cython.boundscheck(False)
cpdef bint color_same_cts2(color_tolerance_setting, unsigned char[:] color):
    cts = color_tolerance_setting
    cdef float r, g, b, c_min, c_max, lum, hue, d
    r = color[2] / 255.0
    g = color[1] / 255.0
    b = color[0] / 255.0

    c_min = min(r, g, b)
    c_max = max(r, g, b)

    lum = 0.5 * (c_max + c_min)
    if abs(lum * 100 - cts.lum) > cts.tolerance:
        return False
    if c_min == c_max:
        if cts.sat <= cts.sat_mod:
            return True
        else:
            return False

    d = c_max - c_min
    if lum < 0.5:
        sat = d / (c_max + c_min)
    else:
        sat = d / (2 - c_max - c_min)

    if abs(sat * 100 - cts.sat) > cts.sat_mod:
        return False
    if r == c_max:
        hue = (g - b) / d
    else:
        if g == c_max:
            hue = 2.0 + (b - r) / d
        else:
            hue = 4 + (r - g) / d
    hue = hue / 6.0
    if hue < 0:
        hue = hue + 1

    hue *= 100;
    if hue > cts.hue:
        return min(hue - cts.hue, abs(hue - (cts.hue + 100))) <= cts.hue_mod
    else:
        return min(cts.hue - hue, abs(cts.hue - (hue + 100))) <= cts.hue_mod
