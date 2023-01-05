#!/usr/bin/python3

"""unittests for max integer in list"""

import unittest
maxi = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        empty = []
        self.assertEqual(maxi(empty), None)

    def test_first(self):
        ls = [7, 4, 2, 5, 1]
        self.assertEqual(maxi(ls), 7)

    def test_one(self):
        ls = [4]
        self.assertEqual(maxi(ls), 4)

    def test_floats(self):
        ls = [2.5, 6.7, 3.2, 5.5]
        self.assertEqual(maxi(ls), 6.7)

    def test_neg(self):
        ls = [-6, 4, 3, 6, -7]
        self.assertEqual(maxi(ls), 6)

    def test_end(self):
        ls = [3, 5 ,6 , 1, 9]
        self.assertEqual(maxi(ls), 9)

    def test_ineg(self):
        ls = [3, 5, 7, -4]
        self.assertEqual(maxi(ls), 7)

    def test_string(self):
        ls = ['cow', 'dog' , 'rat', 'fish']
        self.assertEqual(maxi(ls), 'rat')

if __name__ == '__main__':
    unittest.main()
