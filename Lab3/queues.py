# Design Recipe   implements an efficient first in first out abstract data type using a linked list


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


class Node:
    # Purpose: initialize attribute value and next for Node class
    # Signature: int/string/float-> None
    def __init__(self, newval):
        self.value = newval
        self.next = None
    # Purpose: represent the attributes
    # Signature: None-> None

    def __repr__(self):
        print(self.value)

# Create a queue class that has the attributes to detect empty queue, full queue, push, pop and peek


class QueueLinked:

    # Purpose: initialize attribute value and next for Node class
    # Signature: int-> None
    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.head = None
        self.num_items = 0
        self.tail = None
    # Purpose: represent the attributes
    # Signature: None-> None

    def __repr__(self):
        print(self.head)

    # Purpose: check if the stack is empty, other return false
    # Signature: None->Boolean
    def linkis_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.tail == None:
            return True
        return False

    # Purpose: check if the stack is full
    # Signature: None->Boolean
    def linkis_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if (self.num_items == self.capacity):
            return True
        return False

     # Purpose: Push item into the stack, if full raise Index Error
    # Signature: Int/float/string->list
    def linkenqueue(self, item):
        """If stack is not full, pushes item on stack. 
        If stack is full when push is attempted, raises IndexError"""
        # next becomes head
        x = Node(item)
       : if (self.linkis_empty()):
            self.tail = self.head = x
            self.num_items += 1
        elif(self.num_items < self.capacity)

            self.tail.next = x  # ??????
            # new node becomes tail
            self.tail = x
            self.num_items += 1
        elif(self.capacity == self.num_items):
            raise IndexError

        return self.num_items

    # Purpose: Pop the last item in out of the stack
    # If stack is empty when pop is attempted, raises IndexError"""
    # Signature: None-> int/float/string
    def linkdequeue(self):
        """If stack is not empty, pops item from stack and returns item.
        If stack is empty when pop is attempted, raises IndexError"""

        if self.num_items == 0:
            raise IndexError
        else:
            item = self.head.value
            self.head = self.head.next
            self.num_items -= 1

            return item
      # Purpose: peek the next item that is going to get popped; if empty raise Index Error
    # Signature: None-> int/float/string

    def linkpeek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
        If stack is empty, raises IndexError"""

        if (self.linkis_empty() == False):
            return self.head.value
        else:
            raise IndexError

      # Purpose: size of the stack
    # Signature: None-> int

    def linksize(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
