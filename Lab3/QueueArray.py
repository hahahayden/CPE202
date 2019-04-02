# Contract: Uses capacity, items, num_items, head, and tail to create a queue linked array
# Purpose: implements an efficiient first-in first-out Abstract Data Type


class QueueArray:
   # Initialize the attributes
    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.head = 0
        self.tail = 0
    # Representation of the attributes

    def __repr__(self):
        print(self.items)
        print(self.num_items)

    # returns true if the stack self is empty and false otherwise
    # None-> Boolean
    def is_empty(self):

        if self.num_items == 0:
            return True
        return False

    # Returns true if the stack self is full and false otherwise
    # None-> boolean
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""

        if (self.num_items == self.capacity):
            return True
        return False

    # Purpose; if stack isn't full, push items onto stack
        # if stack is full when push is attempted, raise IndexError
    # Int/float/string-> list
    def enqueue(self, item):

        if (self.items[0] == None):
            self.items[0] = item
            self.tail = 0
            self.num_items += 1
            self.tail += 1
        elif(self.num_items < self.capacity):

            self.items[self.tail] = item
            self.tail += 1
            self.num_items += 1

        elif (self.capacity == self.num_items):
            raise IndexError

        return self.items

    # Purpose:If the stack is not empty, pops item from stack and returns item; if stack is empty when pop is attempted raises IndexError
    # None-> int/ float/string
    def dequeue(self):

        if self.num_items == 0:  # self.head==0 doesnt work
            raise IndexError
        else:
            temp = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head)+1
            self.num_items -= 1
        return temp

    # Purpose: If stack is not empty, returns next item to be popped (but does not pop the item) If stack is empty, raises IndexError"""
    # Signature: None-> int/float/string
    def peek(self):

        if (self.num_items == 0):
            raise IndexError
        else:
            return self.items[self.head]
    # Purpose: returns the number of elements currently in the stack, not the capacity
    # None-> int

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return (self.num_items)


'''

x = QueueArray(3)
x.enqueue(3)
x.enqueue(7)
x.enqueue(8)

print(x.items)
x.dequeue()
print(x.items)
x.enqueue(5)

x.dequeue()
print(x.items)
print(x.tail)
x.enqueue(3)
x.dequeue()
print(x.items)
'''
