# Hayden Tam
# Einakian
# CPE 202-03
# Double Linked List TestCases for Lab4

import unittest


from ordered_list import*


class TestCase(unittest.TestCase):

    def testlinkis_empty(self):
        stack = DoublyLinkedList()
        self.assertTrue(stack.is_empty(), True)
        stack.add(8)
        self.assertFalse(stack.is_empty(), False)
        stack.add(9)
        self.assertFalse(stack.is_empty(), False)

    def test_linkadd(self):
        stack = DoublyLinkedList()
        stack.add(5)
        self.assertEqual(stack.head.data, 5)
        self.assertEqual(stack.tail.data, 5)
        stack.add(3)  # returns length
        self.assertEqual(stack.tail.data, 5)
        self.assertEqual(stack.head.data, 3)
        stack.add(6)
        self.assertEqual(stack.tail.data, 6)

    def test_linkremove(self):
        stack = DoublyLinkedList()
        stack.add(4)
        self.assertEqual(stack.remove(4), 0)

        stack.add(5)
        stack.add(6)
        stack.add(8)
        # self.assertEqual(stack.remove(4), 0)
        self.assertEqual(stack.remove(5), 0)
        self.assertEqual(stack.remove(8), 1)

        self.assertTrue(stack.is_empty, True)
        self.assertEqual(stack.remove(2), -1)

    def test_searchForward(self):
        stack = DoublyLinkedList()
        stack.add(4)
        stack.add(5)
        stack.add(6)
        self.assertEqual(stack.search_forward(4), True)
        self.assertEqual(stack.search_forward(5), True)

    def test_search_backward(self):
        stack = DoublyLinkedList()
        stack.add(4)
        stack.add(5)
        stack.add(10)
        self.assertTrue(stack.search_backward(10), True)
        self.assertFalse(stack.search_backward(20), True)

    def test_size(self):
        stack = DoublyLinkedList()
        stack.add(4)
        self.assertEqual(stack.size(), 1)
        stack.add(5)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

    def test_index(self):
        stack = DoublyLinkedList()
        stack.add(5)
        stack.add(7)
        stack.add(8)
        self.assertEqual(stack.index(5), 0)
        self.assertEqual(stack.index(3), -1)

    def test_pop(self):
        stack = DoublyLinkedList()
        self.assertEqual(stack.pop(), -1)
        stack.add(3)
        stack.add(5)
        stack.add(7)
        stack.add(8)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.pop(0), 3)
        self.assertEqual(stack.size(), 3)

        stack.add(10)
        self.assertEqual(stack.pop(1), 7)
        self.assertEqual(stack.size(), 3)

        self.assertEqual(stack.pop(2), 10)


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
