# Start of unittest - add to completely test functions in exp_eval
# Hayden Tam= test the maxheap
import unittest
from max_heap import *


class test_expressions(unittest.TestCase):
    def test_insert(self):
        heap = MaxHeap(5)
        heap.insert(2)
        heap.insert(10)
        self.assertTrue(heap.insert(3), True)
        self.assertEqual(heap.maxSize, 5)
        self.assertEqual(heap.heapList, [0, 10, 2, 3])

        heap.insert(20)
        self.assertEqual(heap.heapList, [0, 20, 10, 3, 2])

        self.assertEqual(heap.currentSize, 4)
        self.assertEqual(heap.maxSize, 5)
        #self.assertEqual(heap.sizeOfHeap, 5)

        self.assertFalse(heap.insert(15), False)

    def test_findMax(self):
        heap = MaxHeap(5)
        heap.insert(2)
        heap.insert(10)
        heap.insert(3)

        self.assertEqual(heap.find_max(), 10)

        heap.insert(20)
        self.assertEqual(heap.find_max(), 20)
        heap2 = MaxHeap(1)
        self.assertFalse(heap2.find_max(), None)
        heap3 = MaxHeap(2)
        heap3.insert(20)
        heap3.del_max()
        self.assertFalse(heap3.find_max(), False)

    def test_deleteMax(self):
        heap = MaxHeap(8)
        self.assertFalse(heap.del_max(), False)
        heap.insert(10)
        heap.insert(20)
        heap.insert(25)
        heap.insert(35)
        heap.insert(14)

        heap.insert(100)

        heap.insert(200)

        self.assertEqual(heap.heapList, [0, 200, 25, 100, 10, 14, 20, 35])
        self.assertEqual(heap.del_max(), 200)
        self.assertEqual(heap.heapList, [0, 100, 25, 35, 10, 14, 20])
        self.assertEqual(heap.del_max(), 100)
        self.assertEqual(heap.del_max(), 35)
        self.assertEqual(heap.currentSize, 4)
        self.assertEqual(heap.maxSize, 8)

        #self.assertEqual(heap.sizeOfHeap, 5)

    def test_heapContents(self):
        heap = MaxHeap(5)
        heap.insert(2)
        heap.insert(10)
        heap.insert(3)

        self.assertEqual(heap.heap_contents(), [0, 10, 2, 3])
        heap.insert(5)
        self.assertEqual(heap.heap_contents(), [0, 10, 5, 3, 2])

    def test_isEmpty(self):
        heap = MaxHeap(5)
        self.assertTrue(heap.is_empty(), True)

        heap.insert(10)
        self.assertFalse(heap.is_empty(), False)
        heap2 = MaxHeap(5)
        heap2.insert(2)
        heap2.del_max()
        # print(heap.heapList)
        self.assertTrue(heap2.is_empty(), True)

    def test_isFull(self):
        heap = MaxHeap(5)
        heap.insert(2)
        heap.insert(3)
        heap.insert(5)
        heap.insert(3)
        self.assertTrue(heap.is_full(), True)

        heap.del_max()
        self.assertFalse(heap.is_full(), False)

    def test_getHeapCap(self):
        heap = MaxHeap(5)
        self.assertEqual(heap.get_heap_cap(), 5)
        heap2 = MaxHeap()

        self.assertEqual(heap2.get_heap_cap(), 50)

    def test_getHeapSize(self):
        heap = MaxHeap(5)
        heap.insert(2)
        heap.insert(3)
        heap.insert(5)

        self.assertEqual(heap.get_heap_size(), 4)
        heap.insert(10)
        self.assertEqual(heap.get_heap_size(), 5)
        self.assertFalse(heap.insert(10), False)

    def test_heapSortIncrease(self):
        heap = MaxHeap(5)

        self.assertEqual(heap.heap_sort_increase([2, 3, 5]), [2, 3, 5])

        heap2 = MaxHeap(9)
        self.assertEqual(heap2.heap_sort_increase([8, 10, 20, 25, 35, 14, 100, 200]), [
                         8, 10, 14, 20, 25, 35, 100, 200])

        heap3 = MaxHeap(5)
        self.assertEqual(heap3.heap_sort_increase([2, 1, 4, 6]), [1, 2, 4, 6])

    def test_buildHeap(self):
        heap = MaxHeap(2)
        self.assertFalse(heap.build_heap([1, 2]), False)
        heap2 = MaxHeap(6)
        self.assertTrue(heap2.build_heap([1, 2, 3, 4, 5]), True)
        self.assertEqual(heap2.heapList, [0, 5, 4, 3, 1, 2])
        heap3 = MaxHeap(6)
        self.assertTrue(heap3.build_heap([2, 8, 6, 4, 1]), True)
        self.assertEqual(heap3.heapList, [0, 8, 4, 6, 2, 1])
        heap4 = MaxHeap(5)
        self.assertTrue(heap4.build_heap([2, 1, 4, 6]), True)
        self.assertEqual(heap4.heapList, [0, 6, 2, 4, 1])


if __name__ == "__main__":
    unittest.main()
