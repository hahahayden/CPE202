# Hayden

import unittest
from stack_array import *

from stack_linked import*


class TestCase(unittest.TestCase):
    def test_is_full(self):
        stack = StackArray(2)
        self.assertFalse(stack.is_full(), False)
        stack.push(14)
        self.assertFalse(stack.is_full(), False)
        stack.push(15)
        self.assertTrue(stack.is_full(), True)

    def test_is_empty(self):
        stack = StackArray(2)
        self.assertTrue(stack.is_empty(), True)
        stack.push(14)
        self.assertFalse(stack.is_empty(), False)
        stack.push(14)
        self.assertFalse(stack.is_empty(), False)

    def test_push(self):
        stack = StackArray(3)
        self.assertEqual(stack.push(4), [4, None, None])
        self.assertEqual(stack.push(20), [4, 20, None])
        self.assertEqual(stack.push(6), [4, 20, 6])

        with self.assertRaises(IndexError):  # magic - uses context manager
            stack.push(3)

    def test_pop(self):
        stack = StackArray(4)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.num_items, 0)
        stack2 = StackArray(4)
        with self.assertRaises(IndexError):  # magic - uses context manager
            stack2.pop()

    def test_peek(self):
        stack = StackArray(5)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        stack.pop()
        self.assertEqual(stack.peek(), 3)

        stack2 = StackArray(1)
        with self.assertRaises(IndexError):  # magic - uses context manager
            stack2.peek()

    def test_size(self):
        stack = StackArray(5)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

    # Linked List

    def testlinkis_empty(self):
        stack = StackLinked(6)
        self.assertTrue(stack.is_empty(), True)
        stack.push(8)
        self.assertFalse(stack.is_empty(), False)
        stack.push(9)
        self.assertFalse(stack.is_empty(), False)

    def testlinkis_full(self):
        stack = StackLinked(2)
        self.assertFalse(stack.is_full(), False)
        stack.push(6)
        stack.push(8)
        self.assertTrue(stack.is_full(), True)
        stack.pop()
        self.assertFalse(stack.is_full(), False)

    def test_linkpush(self):
        stack = StackLinked(4)
        stack.push(5)
        self.assertEqual(stack.head.value, 5)

        self.assertEqual(stack.push(3), 2)  # returns length
        self.assertEqual(stack.head.value, 3)
        stack.push(6)
        self.assertEqual(stack.head.value, 6)
        self.assertEqual(stack.push("HELLO"), 4)
        self.assertEqual(stack.head.value, "HELLO")
        with self.assertRaises(IndexError):  # magic - uses context manager
            stack.push(4)

    def test_linkpop(self):
        stack = StackLinked(2)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.num_items, 1)
        self.assertEqual(stack.pop(), 4)

        self.assertEqual(stack.head, None)

        self.assertTrue(stack.is_empty, True)
        with self.assertRaises(IndexError):  # magic - uses context manager
            stack.pop()

    def test_linkpeek(self):
        stack = StackLinked(2)
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(6)
        self.assertEqual(stack.peek(), 6)
        stack.push(7)
        self.assertEqual(stack.peek(), 7)

    def test_linksize(self):
        stack = StackLinked(2)
        stack.push(5)
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
