import colorsys


class ColorToleranceSetting:
    def __init__(self, color, tolerance, hue_mod, sat_mod):
        hls = color.get_hls()
        self.hue = hls[0]
        self.lum = hls[1]
        self.sat = hls[2]
        self.hue_mod = tolerance * hue_mod
        self.sat_mod = tolerance * sat_mod
        self.tolerance = tolerance
