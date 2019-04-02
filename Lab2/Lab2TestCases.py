# Name: Hayden Tam
# Section: CPE 202- 04

# Test Cases for Lab2


import unittest
from Lab2 import *


class TestCase(unittest.TestCase):
    def test_permutation(self):

        # Run the unit tests.
        x = "abc"
        self.assertEqual(
            permutate(x), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self. assertEqual(permutate("ab"), ["ab", "ba"])
        z = ""
        with self.assertRaises(ValueError):
            permutate(z)

        self.assertEqual(permutate("a"), "a")
        self.assertEqual(len(permutate("abcde")), 120)


if (__name__ == '__main__'):
    unittest.main()
