# Name: Hayden Tam
# Section: CPE 202- 04

# Test Cases for Lab1

from Lab1 import *

import unittest
from Lab1 import *


class TestCase(unittest.TestCase):
    def test_max_list_iter(self):
        tlist = [10, 9, 8, 4, 9]  # Test Case 1 first half
        self.assertEqual(max_list_iter(tlist), 10)

        clist = [2, 3, 4, 5, 2]  # Test Case 2 second half
        self.assertEqual(max_list_iter(clist), 5)

        plist = [5, 6, 72, 1, 2, 3]  # Test Case 3 middle
        self.assertEqual(max_list_iter(plist), 72)

        # Test Case 4 empty list

        zlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            max_list_iter(zlist)

        qlist = [5]  # Test Case 5 when list is only length of 1
        self.assertEqual(max_list_iter(qlist), 5)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec("abcd"), "dcba")
        self.assertEqual(reverse_rec("dcba"), "abcd")
        self.assertEqual(reverse_rec("efdba"), "abdfe")
        self.assertEqual(reverse_rec("12345"), "54321")
        self.assertEqual(reverse_rec("a"), "a")
        with self.assertRaises(ValueError):
            reverse_rec('')

    def test_bin_search(self):
        # Add code here.
        self.assertEqual(bin_search(
            20, 0, 8, [0, 2, 10, 15, 16, 19, 20, 25, 30]), 6)
        self.assertEqual(bin_search(
            2, 1, 8, [0, 2, 10, 15, 16, 19, 20, 25, 30]), 1)
        self.assertEqual(bin_search(
            16, 0, 8, [0, 2, 10, 15, 16, 19, 20, 25, 30]), 4)
        self.assertEqual(bin_search(
            1, 0, 8, [0, 2, 10, 15, 16, 19, 20, 25, 30]), None)  # Doesn't exist
        self.assertEqual(bin_search(
            19, 0, 8, []), None)  # No list


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
