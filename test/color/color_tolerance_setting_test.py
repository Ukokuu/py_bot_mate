import unittest

from py_bot_mate.color.color import Color
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting


class ColorToleranceSettingTest(unittest.TestCase):

    def test_create_color_tolerance_setting_correctly(self):
        cts = ColorToleranceSetting(Color(64, 87, 117), 1, 0.29, 3.60)
        self.assertAlmostEqual(59.43396226415093, cts.hue)
        self.assertAlmostEqual(35.49019607843137, cts.lum)
        self.assertAlmostEqual(29.281767955801108, cts.sat)
        self.assertAlmostEqual(0.29, cts.hue_mod)
        self.assertAlmostEqual(3.60, cts.sat_mod)
        self.assertAlmostEqual(1, cts.tolerance)


if __name__ == '__main__':
    unittest.main()
