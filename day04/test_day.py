import unittest
import day04.day as day
import day04.helper as helper


class TestBingo(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(2, 2)
        self.assertEqual(3, 3)

    def test_part_1a(self):
        expected = 4512
        result = day.alg1(helper.input_as_lines("day04/test.txt"), False)
        self.assertEqual(expected, result)
    
    def test_part_1b(self):
        expected = 72770
        result = day.alg1(helper.input_as_lines("day04/input.txt"), False)
        self.assertEqual(expected, result)
    
    def test_part_2a(self):
        expected = 1924
        result = day.alg2(helper.input_as_lines("day04/test.txt"), False)
        self.assertEqual(expected, result)

    def test_part_2b(self):
        expected = 13912
        result = day.alg2(helper.input_as_lines("day04/input.txt"), False)
        self.assertEqual(expected, result)
    

if __name__ == '__main__':
    unittest.main()