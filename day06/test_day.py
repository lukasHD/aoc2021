import os
import unittest

import day06.day as day
import day06.helper as helper
"""
    part1(test_fname, 18, True)
    part1(test_fname, 80, True)
    part1(input_fname, 80)
    part2(test_fname, 256, True)
    part2(input_fname, 256)
"""

class TestDay(unittest.TestCase):
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    def test_part_1a1(self):
        expected = 26
        result = day.alg1(helper.single_line_as_ints(self.test_fname), 18, False)
        self.assertEqual(expected, result)

    def test_part_1a2(self):
        expected = 5934
        result = day.alg1(helper.single_line_as_ints(self.test_fname), 80, False)
        self.assertEqual(expected, result)
    
    def test_part_1b(self):
        expected = 350149
        result = day.alg1(helper.single_line_as_ints(self.input_fname), 80, False)
        self.assertEqual(expected, result)
    
    def test_part_2a(self):
        expected = 26984457539
        result = day.alg2(helper.single_line_as_ints(self.test_fname), 256, False)
        self.assertEqual(expected, result)

    def test_part_2b(self):
        expected = 1590327954513
        result = day.alg2(helper.single_line_as_ints(self.input_fname), 256, False)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()