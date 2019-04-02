# Hayden Tam
# Lab7: Max Heap
# Sussan Einakian

# build a max heap that allows you to insert and delete the max value, while allowing access to heap size

# Be able to percolate up and down the tree


class MaxHeap():
    # Initialize attributes of heaplist, currentsize (shows the size of what is in the heap not including 0)
    # maxsize, shows the max capacity; and size of heap shows the size of the heap including the starting 0
    def __init__(self, capacity=50):
        self.heapList = [0]
        self.currentSize = 0  # currentSize of the things added
        self.maxSize = capacity  # capacity includes the 0
        # self.sizeOfHeap = self.currentSize+1  # size of the heap

    def __repr__(self):
        return self.heapList and self.currentSize

    # Insert a number into the heap tree and percolate up to find its right location
    # Sig: int/float-> None
    def insert(self, item):

        if (self.maxSize-1 <= self.currentSize):
            return False
        else:
            self.heapList.append(item)
            self.currentSize = self.currentSize + 1
            # self.percUp(self.currentSize)

            #self.sizeOfHeap += 1

            self.perc_up(self.currentSize)
            return True

    # Find maximum value in the tree
    # Sig: none-> int/float

    def find_max(self):
        if (len(self.heapList) == 1):
            return None
        else:
            return self.heapList[1]
    # Delete the max value in the tree and then find replacement ; returns the deleted max
    # Sig: None-> Bool/int/float

    def del_max(self):
        if (len(self.heapList) == 1):
            return False

        temp = self.find_max()
        # print(self.heapList[1])

        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.perc_down(1)
        #self.sizeOfHeap -= 1

        print(temp)
        return temp

    # Shows the contents within the heap tree
    # Sig: None-> List
    def heap_contents(self):
        return self.heapList

    # Shows if the tree is empty
    # Sig: None-> bool
    def is_empty(self):
        if(len(self.heapList) == 1):
            return True
        else:
            return False

    # Shows if the tree is full; includes the starting 0

    # Sig: None-> bool
    def is_full(self):
        if (self.currentSize+1 == self.maxSize):
            return True
        else:
            return False

    # Gets the max capacity of the heap; includes the zero
    # Sig: None-> int
    def get_heap_cap(self):
        return self.maxSize

    # Gets the current size of the heap tree inludign the zero

    # None-> int
    def get_heap_size(self):
        return self.currentSize+1

    # Helper function to percolate through the tree; goes up the tree
    # int -> none

    def perc_up(self, i):
        while i // 2 > 0:

            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            # print(self.heapList)
            i = i // 2
            # print(self.heapList)

    # Percolates down a tree
    # Int -> None

    def perc_down(self, i):
        # 2*i is left child, 2*i+1 is right child
        # print(i)
        while (2*i) <= self.currentSize:
            greater = 2*i  # greater sibling assumed is left child
            if not 2*i+1 > self.currentSize:
                if self.heapList[2*i] < self.heapList[2*i+1]:
                    greater = 2*i+1  # greater sibling is right child
            # if item is lesser than greatest child
            if self.heapList[i] < self.heapList[greater]:
                # swap
                self.heapList[i], self.heapList[greater] = self.heapList[greater], self.heapList[i]
            # print(self.heapList)
            i = greater
            # print(i)

    # Builds a heap from a given list
    # List-> list
    def build_heap(self, alist):

        # print(self.sizeOfHeap)
        if (len(alist) >= self.maxSize):

            return False

        i = len(alist)//2
        # i = len(alist)
        self.currentSize = len(alist)
        self.heapList = [0]+alist[:]
        while i > 0:
            self.perc_down(i)
            # self.perc_up(self.currentSize)
            i -= 1

        # return self.heapList
        return True
 # Takes a list builds a heap and returns a list in increasing order
    # List-> List

    def heap_sort_increase(self, alist):
        res = []
        # = MaxHeap()
        self.build_heap(alist)
        for _ in range(1, len(self.heapList)):
            res.insert(0, self.del_max())
        return res


'''

heap = MaxHeap(5)
heap.insert(2)
heap.insert(3)
heap.insert(5)
heap.insert(1)
print(heap.maxSize)
print(heap.currentSize)
print(heap.heapList)
print(heap.is_full())
heap.del_max()

print(heap.is_full())
print(heap.heapList)
# print(heap.get_heap_size)
'''
x = MaxHeap(15)
#x.build_heap([0, 1])
print(x.heap_sort_increase([15, 17, 30, 3, 14, 2, 27, 9, 21, 10, 20]))

# print(x.build_heap([1, 2, 3, 4, 5]))
x2 = MaxHeap()
# print(x2.build_heap([2, 1, 4, 6]))
# print(x2.build_heap([12, 6, 5, 89, 13, 25, -5, 14, 28, 10]))
# print(x.heap_sort_increase([5, 12, 64, 1, 37, 90, 91, 97]))
# print(x.heap_sort_increase([1, 2, 3, 4, 5]))
# print(x.build_heap([2, 1, 4, 6]))
# rint(x.heapList)
'''


x = MaxHeap()
x.insert(10)
print(x.heapList[0])
x.insert(20)
x.insert(25)
x.insert(35)
x.insert(14)

x.insert(100)

x.insert(200)
print(x.heapList[1])
print(x.heapList[2])
print(x.heapList[3])

print(x.find_max())
print(x.currentSize)
print(x.heapList)
# print(x.del_max())
print(x.heapList)

# print(x.get_heap_size())
print(x.heap_sort_increase())
'''
