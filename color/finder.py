# TCTS2Info = record
# H, S, L: extended;
# hueMod, satMod: extended;
# Tol: Integer;
# end;

# Result := AllocMem(SizeOf(TCTS2Info));
# ColorToRGB(Color, R, G, B);
# RGBToHSL(R, G, B, PCTS2Info(Result)^.H, PCTS2Info(Result)^.S,
#                                                            PCTS2Info(Result)^.L);
# PCTS2Info(Result)^.hueMod := Tol * hueMod;
# PCTS2Info(Result)^.satMod := Tol * satMod;
# PCTS2Info(Result)^.Tol := Tol;

# function Create_CTSInfo_helper(cts: integer; Color, Tol: Integer;
# hueMod, satMod, CTS3Modifier: extended): Pointer; overload;

import colorsys


class Finder:

    @staticmethod
    def color_same_cts2(color_tolerance_setting, color):
        cts = color_tolerance_setting
        r = color.r / 255
        g = color.g / 255
        b = color.b / 255

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
                hue = 2 * (b - r) / d
            else:
                hue = 4 + (r - g) / d
        hue = hue / 6;
        if hue < 0:
            hue = hue + 1

        if hue > cts.hue:
            return min(hue - cts.hue, abs(hue - (cts.hue + 100))) <= cts.hue_mod
        else:
            return min(cts.hue - hue, abs(cts.hue - (hue + 100))) <= cts.hue
