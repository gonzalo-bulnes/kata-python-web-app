# coding=utf-8

import os
from test.support import EnvironmentVarGuard
import unittest

import numbersandcolors

class TestNumbersAndColors(unittest.TestCase):

    def test_lucky_number_is_an_integer(self):
        lucky_number = numbersandcolors.lucky_number()
        self.assertIsInstance(lucky_number, int, "expected lucky_number to return an integer")

    def test_lucky_color_is_a_string(self):
        lucky_color = numbersandcolors.lucky_color()
        self.assertIsInstance(lucky_color, str, "expected lucky_color to return a string")

    def test_lucky_color_defaults_to_purple(self):
        lucky_color = numbersandcolors.lucky_color()
        self.assertEqual(lucky_color, 'purple', "expected default lucky_color to be 'purple'")

    def test_lucky_color_is_read_from_environemt(self):
        self.env = EnvironmentVarGuard()
        self.env.set('COLOR', 'green')
        lucky_color = numbersandcolors.lucky_color()
        self.assertEqual(lucky_color, 'green', "expected lucky_color to be 'green'")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumbersAndColors)
    unittest.TextTestRunner(verbosity=2).run(suite)
