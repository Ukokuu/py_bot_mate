import unittest

from py_bot_mate.color.finder import Finder
from py_bot_mate.color.color import Color
from py_bot_mate.color.color_tolerance_setting import ColorToleranceSetting


class FinderTest(unittest.TestCase):

    def test_find_similar_colors(self):
        cts = ColorToleranceSetting(Color.from_bgr(4011880), 2, 0.38, 2.50)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3881055))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3945837))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3946098))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(4798250))
        self.assertFalse(result)

    def test_find_similar_colors2(self):
        cts = ColorToleranceSetting(Color.from_bgr(6107474), 6, 3.26, 0.86)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3881055))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3945837))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(3946098))
        self.assertTrue(result)
        result = Finder.color_same_cts2(cts, Color.from_bgr(4798250))
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
