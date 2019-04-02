#Design Recipe: Create a node class and a double linked list that can create a ordered double linked list, with adding and removing functions.
#Data Defintion for Node Class: data= int; next=None; previous=None
class Node:
    def __init__(self, itemData):
        self.data = itemData
        self.next = None
        self.previous = None
    
 #Data Definition for DoublyLinkedList Class: 
 #a double linked list has the attributes of head (Node) tail (Node) and num_items(int)

class DoublyLinkedList:
    #Purpose: initialize attributes
    #Signature: None-> None
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    #Purpose: to check if the doubly linked list is empty; if not return false
    #Signature: None-> NOne

    def is_empty(self):
        if(self.head is None):
            return True
        else:
            return False
    #purpose: to add items in a sorted manner
    #Signature: Int-> None

    def add(self, item):
        currentNode = self.head

        previousNode = None
        stopLoop = False
        while((currentNode != None) and not(stopLoop)):
   
            if (currentNode.data > item):
                stopLoop = True

            else:
                previousNode = currentNode
                currentNode = currentNode.next

        temp = Node(item)
        # If the List is Empty set the tail and head to the element
        if(previousNode == None and currentNode == None):
            # temp.setNext(self.head)
            temp.next = self.head
            self.head = temp
            self.tail = temp
            self.num_items += 1
        # If the item to be added needs to be at the beginning
        elif(previousNode == None):
            temp.next=self.head
            self.head = temp.previous
            self.head = temp

            self.num_items += 1
        # If the item to be added has to be at the end
        elif(currentNode == None):
         
            temp.previous = self.tail
            
            self.tail.next = temp
            self.tail = temp
            self.num_items += 1

        # If the item to be added has to be in th middle
        else:
       
            temp.next = currentNode
         
            temp.prev = previousNode
   
            previousNode.next = temp
     
            currentNode.prev = temp
            self.num_items += 1

    #Purpose: remove a specified integer from the sorted list; once found it removes it and returns the position that it was found at
                #if item isn't found returns -1
    #Signature: int-> int
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        count = 0
        while(current != None and not(found)):
            if(current.data == item):
                found = True

            else:
                previous = current
                current = current.next
                count += 1
        # Removing item at beginning
        if(current == None):
            return -1

        elif(previous == None):
            if(current.next != None):
                self.head = current.next
                self.num_items -= 1
                self.head.previous=(None)
            elif(current.next == None):
                self.head.previous=None
                self.head.next=(None)
                self.head = None
                self.tail = None
                self.num_items -= 1

        # Removing item at the end
        elif(current.next == None):
            self.num_items -= 1
          
            self.tail = self.tail.previous
      
            self.tail.next = None
        # Removing in the middle
        else:
         
            previous.next = current.next
          
            current.next.previous = previous
          
            self.num_items -= 1
        return count

    #purpose: search for an item using head and returns True if found and if not returns false
    #Signature: int-> bool
    def search_forward(self, item):

        current = self.head
        found = False
        while(current != None and not(found)):
            if(current.data == item):
                found = True
            else:
                current = current.next
        return found
    #Purpose: search from the tail and backwards to find an item; returns True if found if not false
    #Signature: int-> bool
    def search_backward(self, item):
        current = self.tail
        found = False
        while(current != None and not(found)):
            if(current.data == item):

                found = True
            else:
                current = current.previous
          
        return found
    #Purpose: returns the size of the double linked list
    #Signature: none-> int
    def size(self):
        return self.num_items
    #Purpose: returns the index of an item
            # if item isn't found; returns -1
    #Signature: int-> int
    def index(self, item):
        current = self.head
        index = 0
        while(current != None):
            if(current.data == item):
                return index
            else:
                index += 1
                current = current.next
        return -1
    #Purpose: pops the item from the list; can either be a specified index or not; if not it pops the last element
    #Signature: None/int-> int
    def pop(self, index=None):
        if index == None:
            current = self.tail
    # Removing at the tail
            x = current.data
            self.tail = self.tail.previous
            
            self.tail.next = None
            self.num_items -= 1
            return x
        current = self.head
        previous = None
        if index < 0 or index > self.size():
            raise IndexError
        for i in range(index):
            previous = current
            current = current.getNext()

        if index == 0:  # Removing at the head
            x = current.data
            if (current.next != None):  # if it isn't the only one
                self.head = self.head.next
                self.head.setPrevious(None)
                self.num_items -= 1
            if (current.next == None):  # take it out
                self.head.previous=None
                self.head.next=None
                self.head = None
                self.tail = None
                self.num_items -= 1
            return x

        else:  # Removing in the middle of the list
            x = current.data
            #previous.setNext(current.next)
            previous.next=current.next
            previous=previous.next
            # current.getNext().setPrevious(previous)
            current.next = previous
            self.num_items -= 1
            
            return x

  