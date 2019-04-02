# Hayden Tam
# Einakian
# CPE 202-03
# StackArray for Project 1

# Implements an efficient last-in first-out Abstract Data Type using Python List


class StackArray:

    # Initialize variables
    # Create an empty stack with a capacity
    # Signature: Int-> None
    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.head = 0
        self.tail = 0
    # Represent variables
    # Signature: None-> NOne

    def __repr__(self):
        print(self.items)
        print(self.num_items)
    # Purpose: check if stack is empty
    # Signature: None-> Boolean

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if self.num_items == 0:
            return True
        return False

    # Purpose: check if stack is full
    # Signature: None-> Boolean
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""

        if (self.num_items == self.capacity):
            return True
        return False

    # Purpose: push items into the stack; if full raise IndexError
    # Signature: int/float/string-> list

    def push(self, item):
        """If stack is not full, pushes item on stack.
        If stack is full when push is attempted, raises IndexError"""

        if (self.items[0] == None):
            self.items[0] = item

            self.num_items += 1

        elif(self.num_items < self.capacity):
            self.head += 1
            self.items[self.head] = item
            self.num_items += 1
        elif (self.capacity == self.num_items):
            raise IndexError
        return self.items

    # Purpose: Pop elements from the end of list; last in first out; if zero elements raise IndexError
    # Signature: NOne-> int/float/string
    def pop(self):
        """If stack is not empty, pops item from stack and returns item.
        If stack is empty when pop is attempted, raises IndexError"""

        if self.num_items == 0:  # self.head==0 doesnt work
            raise IndexError
        else:
            temp = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head)-1
            self.num_items -= 1
        return temp

    # Purpose; peek the next element to be popped; if stack empty raise IndexError
    # Signatuer: None-> int/float/string
    def peek(self):

        if (self.num_items == 0):
            raise IndexError
        else:
            return self.items[self.head]
    # Purpose: find size of stack
    # Signature: None-> int

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return (self.num_items)


'''
count = 0
x = StackArray(6)
print(x.is_full())
x.push(7)
x.push(8)
x.push(1)
print(x.pop())
x.push(1)
print(x.peek())  # 8
print(x.size())  # 2
print(x.items)
print(x.num_items)



'''
