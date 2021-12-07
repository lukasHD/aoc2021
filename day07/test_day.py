import os
import unittest

# import day07.day as day
# import day07.helper as helper
import day
import helper 


class TestDay(unittest.TestCase):
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    def test_part_1a(self):
        expected = 37
        result = day.alg1(helper.single_line_as_ints(self.test_fname), False)
        self.assertEqual(expected, result)
    
    def test_part_1b(self):
        expected = 349769
        result = day.alg1(helper.single_line_as_ints(self.input_fname), False)
        self.assertEqual(expected, result)
    
    def test_part_2a(self):
        expected = 168
        result = day.alg2(helper.single_line_as_ints(self.test_fname), False)
        self.assertEqual(expected, result)

    def test_part_2b(self):
        expected = 99540554
        result = day.alg2(helper.single_line_as_ints(self.input_fname), False)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()