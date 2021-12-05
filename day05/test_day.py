import os
import unittest

import day__.day as day
import day__.helper as helper


class TestDay(unittest.TestCase):
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    def test_part_1a(self):
        expected = 0
        result = day.alg1(helper.input_as_lines(self.test_fname), False)
        self.assertEqual(expected, result)
    
    def test_part_1b(self):
        expected = 0
        result = day.alg1(helper.input_as_lines(self.input_fname), False)
        self.assertEqual(expected, result)
    
    def test_part_2a(self):
        expected = 0
        result = day.alg2(helper.input_as_lines(self.test_fname), False)
        self.assertEqual(expected, result)

    def test_part_2b(self):
        expected = 0
        result = day.alg2(helper.input_as_lines(self.input_fname), False)
        self.assertEqual(expected, result)
