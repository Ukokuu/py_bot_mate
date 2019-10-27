import colorsys


class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_hls(self):
        [hue, lum, sat] = colorsys.rgb_to_hls(self.r / 255, self.g / 255, self.b / 255)
        hue *= 100
        lum *= 100
        sat *= 100
        return [hue, lum, sat]

    def to_array(self):
        return [self.r, self.g, self.b]

    @staticmethod
    def from_bgr_values(bgr_array):
        return Color(bgr_array[2], bgr_array[1], bgr_array[0])

    @staticmethod
    def from_bgr(color_value):
        hex_value = format(color_value, 'x')
        return Color.from_bgr_hex(hex_value)

    @staticmethod
    def from_bgr_hex(hex_value):
        b = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        r = int(hex_value[4:6], 16)
        return Color(r, g, b)
