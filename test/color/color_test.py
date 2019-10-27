import unittest

from py_bot_mate.color.color import Color


class ColorTest(unittest.TestCase):

    def test_get_hls(self):
        color = Color(178, 183, 163)
        hls = color.get_hls()
        self.assertAlmostEqual(20.83333333333334, hls[0])
        self.assertAlmostEqual(67.84313725490196, hls[1])
        self.assertAlmostEqual(12.195121951219521, hls[2])

    def test_bgr_hex(self):
        hex_value = '755740'
        color = Color.from_bgr_hex(hex_value)
        self.assertEqual(color.r, 64)
        self.assertEqual(color.g, 87)
        self.assertEqual(color.b, 117)

    def test_bgr(self):
        color_value = 4011376
        color = Color.from_bgr(color_value)
        self.assertEqual(color.r, 112)
        self.assertEqual(color.g, 53)
        self.assertEqual(color.b, 61)



if __name__ == '__main__':
    unittest.main()
