# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_valid(self):
        
        self.assertTrue(postfix_valid("3 5 -"), True)

        try:
            postfix_valid("+ 4 3")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Not valid postfix")
        self.assertTrue(postfix_valid("6"), True)

        try:
            postfix_valid("4 + 5")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        try:
            postfix_valid("+ +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient Operands")

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 -5.2 +"), -2.2)
        self.assertAlmostEqual(postfix_eval("2 3 2 ^ ^"), 512)
        self.assertAlmostEqual(postfix_eval("2 3 ^"), 8)
        self.assertAlmostEqual(postfix_eval("7 2.1 -"), 4.9)
        self.assertAlmostEqual(postfix_eval("4 3 /"), 1.3333333333)
        self.assertAlmostEqual(postfix_eval("2 7 * 6 / 4 - 2 / 5 +"), 4.1666666666667)
        self.assertAlmostEqual(postfix_eval('2 3 1 * + 9 -'), -4)
        self.assertAlmostEqual(postfix_eval('4 2 3 5 1 - + * +'), 18)
        try:
            postfix_eval(1)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Not string formatted")
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

        try:
            postfix_eval("9 blah +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

        try:
            postfix_eval("+ 9")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Not valid postfix")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 + *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        with self.assertRaises(ValueError):  # magic - uses context manager
            postfix_eval("4 0 / 2 +")

        try:
            postfix_eval("4 5")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        try:
            postfix_eval("1 2 9 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix(
            "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +")
        self.assertEqual(infix_to_postfix(
            ("3 / -4 ^ 6 - 10")), "3 -4 6 ^ / 10 -")
        self.assertEqual(infix_to_postfix(
            "( A + B ) * ( C + D )"), "A B + C D + *")
        self.assertEqual(infix_to_postfix(
            "( A + B ) * C * D"), 'A B + C * D *')
        self.assertEqual(infix_to_postfix(
            "( 1000 + 2 ) * 6 * 8"), '1000 2 + 6 * 8 *')
        self.assertEqual(infix_to_postfix(
            "2 ^ 3 ^ 2"), '2 3 2 ^ ^')

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix(
            "* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix(" * + A B - C D"), "A B + C D - *")
        self.assertEqual(prefix_to_postfix(
            "* - A / B C - / A K L"), "A B C / - A K / L - *")
        self.assertEqual(prefix_to_postfix('+ / - / * 2 7 6 4 2 5'),'2 7 * 6 / 4 - 2 / 5 +')


if __name__ == "__main__":
    unittest.main()
