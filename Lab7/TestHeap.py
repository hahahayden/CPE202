class MaxHeap:
    # initializes empty MaxHeap with default capacity of 50
    # MaxHeap is implemented as an array where left child has index i*2 and right child has index i*2+1
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.heaplist = [None]

    # Inserts item into heap, returns true if successful
    # int -> boolean
    def insert(self, item):
        if self.is_full():
            return False
        self.size += 1
        self.heaplist.append(item)
        if self.size > 1:
            # if item is greater than parent
            if item > self.heaplist[self.size//2]:
                self.perc_up(self.size)
        return True

    # returns max item in heap
    # -> int / None
    def find_max(self):
        return self.heaplist[1]

    # Returns max and removes it from heap, maintaining heap properties
    # -> int / None
    def del_max(self):
        if self.is_empty():
            return None
        res = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        self.perc_down(1)
        return res

    # Returns list of contents of the heap
    # -> list
    def heap_contents(self):
        return self.heaplist

    # takes a list of ints and builds the heap using bottom up
    # list -> boolean
    def build_heap(self, alist):
        if len(alist) > self.capacity:
            return False
        self.size = len(alist)
        self.heaplist = [None] + alist[:]
        i = self.size
        end = i//2
        while i > end:
            self.perc_up(i)
            i -= 1
        self.perc_up(self.size)
        return True

    # Returns true if empty
    # -> boolean
    def is_empty(self):
        return self.size == 0

    # Returns true if full
    # -> boolean
    def is_full(self):
        return self.size == self.capacity

    # Returns capacity of heap
    # -> int
    def get_heap_cap(self):
        return self.capacity

    # Returns size of int
    # -> int
    def get_heap_size(self):
        return self.size

    # Compares item to child, swaps if child is greater, repeats until in proper place
    # int ->
    def perc_down(self, i):
        # 2*i is left child, 2*i+1 is right child
        while (2*i) <= self.size:
            greater = 2*i  # greater sibling assumed is left child
            if not 2*i+1 > self.size:
                if self.heaplist[2*i] < self.heaplist[2*i+1]:
                    greater = 2*i+1  # greater sibling is right child
            # if item is lesser than greatest child
            if self.heaplist[i] < self.heaplist[greater]:
                # swap
                self.heaplist[i], self.heaplist[greater] = self.heaplist[greater], self.heaplist[i]
            i = greater

    # Compares item to parent, swaps if parent is lesser, repeats until in proper place
    # int ->
    def perc_up(self, i):
        # i//2 is the index of the parent
        while (i//2) > 0:
            if self.heaplist[i] > self.heaplist[i//2]:  # if item is greater than parent
                # swap
                self.heaplist[i], self.heaplist[i //
                                                2] = self.heaplist[i//2], self.heaplist[i]
            i = i//2

# Takes a list of integers and returns the list in increasing order using a heap
# list -> list


def heap_sort_increase(alist):
    res = []
    heap = MaxHeap()
    heap.build_heap(alist)
    for _ in range(1, len(heap.heaplist)):
        res.insert(0, heap.del_max())
    return res


x = MaxHeap()
#x.build_heap([2, 1, 4, 6])
print(heap_sort_increase([2, 1, 4, 6]))
print(x.heaplist)
