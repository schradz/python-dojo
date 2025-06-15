import unittest
from sum_digits import *

class test_sum_digits(unittest.TestCase):
    '''Test cases for program that sums together the individual digits of a number'''

    def test_extract_digits(self):
        '''Do double digit and three digit numbers work?'''
        num = 49
        extracted_digits = [9, 4]
        self.assertEqual(extracted_digits, extract_digits(49))
        extracted_digits = [3, 2, 1]
        self.assertEqual(extracted_digits, extract_digits(123))


    def test_sum_digits(self):
        '''Do double digit and three digit numbers work?'''
        num = 49
        sum = 13
        self.assertEqual(sum, sum_digits(49))
        num = 123
        sum = 6
        self.assertEqual(sum, sum_digits(123))

    
if __name__ == '__main__':
    unittest.main()