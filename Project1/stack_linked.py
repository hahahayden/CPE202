# Hayden Tam
# S Einakian CPE 202-03
#  Stack Project 1
# Stack_Linked

# Design: create a node class that has a value and a next value


class Node:
    # initialize variables
    # int/float/string-> None
    def __init__(self, newval):
        self.value = newval
        self.next = None
    # Represent the variables

    # None->None
    def __repr__(self):
        print(self.value)

# Design: create a stack class that detects a empty stack or full stack, while being able to push and pop items and show stack size


class StackLinked:
    """Implements an efficient last-in first-out Abstract Data Type using a Linked List"""
    # initialize variables
    # Creates an empty stack with a capacity
    # Signature: int-> None

    def __init__(self, capacity):

        self.capacity = capacity
        self.head = None
        self.num_items = 0
    # Represent the variables
    # Signature: None-> None

    def __repr__(self):
        print(self.head)

    # Purpose: check if the stack is empty, other return false
    # Signature: None->Boolean

    def is_empty(self):

        if self.head == None:
            return True
        return False

    # Purpose: check if the stack is full
    # Signature: None->Boolean
    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if (self.num_items == self.capacity):
            return True
        return False

    # Purpose: Push item into the stack, if full raise Index Error
    # Signature: Int/float/string->list
    def push(self, item):
        """If stack is not full, pushes item on stack. 
        If stack is full when push is attempted, raises IndexError"""
        # next becomes head
        x = Node(item)

        if(self.num_items < self.capacity):
            x.next = self.head  # new node becomes head
            self.head = x
            self.num_items += 1
        elif(self.capacity == self.num_items):
            raise IndexError

        return self.num_items

    # Purpose: Pop the last item in out of the stack
    # If stack is empty when pop is attempted, raises IndexError"""
    # Signature: None-> int/float/string
    def pop(self):

        if self.num_items == 0:
            raise IndexError
        else:
            item = self.head.value
            self.head = self.head.next

            self.num_items -= 1
            return item

    # Purpose: peek the next item that is going to get popped; if empty raise Index Error
    # Signature: None-> int/float/string
    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
        If stack is empty, raises IndexError"""

        if (self.is_empty() == False):
            return self.head.value
        else:
            raise IndexError

    # Purpose: size of the stack
    # Signature: None-> int
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
