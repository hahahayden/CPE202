
import unittest


from queues import*


class TestCase(unittest.TestCase):
    def test_is_full(self):
        queue = QueueArray(2)
        self.assertFalse(queue.is_full(), False)
        queue.enqueue(14)
        self.assertFalse(queue.is_full(), False)
        queue.enqueue(15)
        self.assertTrue(queue.is_full(), True)

    def test_is_empty(self):
        queue = QueueArray(2)
        self.assertTrue(queue.is_empty(), True)
        queue.enqueue(14)
        self.assertFalse(queue.is_empty(), False)
        queue.enqueue(14)
        self.assertFalse(queue.is_empty(), False)

    def test_enqueue(self):
        queue = QueueArray(3)
        self.assertEqual(queue.enqueue(4), [4, None, None])
        self.assertEqual(queue.enqueue(20), [4, 20, None])
        self.assertEqual(queue.enqueue(6), [4, 20, 6])

        queue.dequeue()
        self.assertEqual(queue.enqueue(2), [2, 20, 6])
        queue.dequeue()  # Take out 20

        self.assertEqual(queue.enqueue(4), [2, 4, 6])
        queue.dequeue()
        self.assertEqual(queue.items, [2, 4, None])
        queue.enqueue(4)
        with self.assertRaises(IndexError):  # magic - uses context manager
            queue.enqueue(3)

    def test_dequeue(self):
        queue = QueueArray(4)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)

        queue2 = QueueArray(4)
        with self.assertRaises(IndexError):  # magic - uses context manager
            queue2.dequeue()

    def test_peek(self):
        queue = QueueArray(5)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(queue.peek(), 3)
        queue.dequeue()
        self.assertEqual(queue.peek(), 4)

        queue2 = QueueArray(1)
        with self.assertRaises(IndexError):  # magic - uses context manager
            queue2.peek()

    def test_size(self):
        queue = QueueArray(5)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(queue.size(), 2)
        queue.dequeue()
        self.assertEqual(queue.size(), 1)

    # Linked list

    def testis_empty(self):
        queue = QueueLinked(6)
        self.assertTrue(queue.linkis_empty(), True)
        queue.linkenqueue(8)
        self.assertFalse(queue.linkis_empty(), False)
        queue.linkenqueue(9)
        self.assertFalse(queue.linkis_empty(), False)

    def testis_full(self):
        queue = QueueLinked(2)
        self.assertFalse(queue.linkis_full(), False)
        queue.linkenqueue(6)
        queue.linkenqueue(8)
        self.assertTrue(queue.linkis_full(), True)
        queue.linkdequeue()
        self.assertFalse(queue.linkis_full(), False)

    def test_linkenqueue(self):
        queue = QueueLinked(3)
        queue.linkenqueue(5)
        self.assertEqual(queue.head.value, 5)
        self.assertEqual(queue.linkenqueue(3), 2)
        self.assertEqual(queue.tail.value, 3)
        self.assertEqual(queue.head.value, 5)
        queue.linkenqueue(6)
        self.assertEqual(queue.tail.value, 6)

        with self.assertRaises(IndexError):  # magic - uses context manager
            queue.linkenqueue(4)

    def test_linkdequeue(self):
        queue = QueueLinked(4)
        queue.linkenqueue(4)
        queue.linkenqueue(5)
        queue.linkenqueue(7)
        self.assertEqual(queue.linkdequeue(), 4)
        self.assertEqual(queue.tail.value, 7)
        self.assertEqual(queue.head.value, 5)
        queue.linkdequeue()
        queue.linkdequeue()

        with self.assertRaises(IndexError):  # magic - uses context manager
            queue.linkdequeue()

    def test_linkpeek(self):
        queue = QueueLinked(2)
        with self.assertRaises(IndexError):
            queue.linkpeek()
        queue.linkenqueue(6)
        self.assertEqual(queue.linkpeek(), 6)

        queue.linkenqueue(7)
        queue.linkdequeue()
        self.assertEqual(queue.linkpeek(), 7)

    def test_linksize(self):
        queue = QueueLinked(2)
        queue.linkenqueue(5)
        self.assertEqual(queue.linksize(), 1)
        queue.linkdequeue()
        self.assertEqual(queue.linksize(), 0)



# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
