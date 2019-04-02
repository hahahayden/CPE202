class Node:
    def __init__(self,itemData):
        self.data = itemData
        self.next = None
        self.previous = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setNext(self,newNext):
        self.next = newNext

    def getPrevious(self):
        return self.previous
    
    def setPrevious(self,newPrevious):
        self.previous = newPrevious
        

class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        currentNode = self.head
        previousNode = None
        stopLoop = False
        while((currentNode != None) and not(stopLoop)):
            if(currentNode.getData() > item):
                stopLoop = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()
        temp = Node(item)
        # If the List is Empty set the tail and head to the element
        if(previousNode == None and currentNode == None):
            temp.setNext(self.head)
            self.head = temp
            self.tail = temp
        #If the item to be added needs to be at the beginning
        elif(previousNode == None):
            temp.setNext(self.head)
            self.head.setPrevious(temp)
            self.head = temp
        #If the item to be added has to be at the end
        elif(currentNode == None):
            temp.setPrevious(self.tail)
            self.tail.setNext(temp)
            self.tail = temp
        #If the item to be added has to be in th middle
        else:
            temp.setNext(currentNode)
            temp.setPrevious(previousNode)
            previousNode.setNext(temp)
            currentNode.setPrevious(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while(current != None and not(found)):
            if(current.getData() == item):
                found = True
            else:
                previous = current
                current = current.getNext()
        #Removing item at beginning
        if(current == None):
            return False
        if(previous == None):
            self.head = current.getNext()
            self.head.setPrevious(None)
        #Removing item at the end
        elif(current.getNext() == None):
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        #Removing in the middle
        else:
            previous.setNext(current.getNext())
            current.getNext().setPrevious(previous)
        return found


    def index(self, item):
        current = self.head
        index = 0
        while(current != None):
            if(current.getData() == item):
                return index
            else:
                index += 1
                current = current.getNext()
        return None

    def pop(self, index):
        current = self.head
        previous = None
        if index < 0 or index > self.size():
            raise IndexError
        for i in range (index):
            previous = current
            current = current.getNext()
        if index == 0: # Removing at the head
            x = current.getData()
            self.head = self.head.getNext()
            self.head.setPrevious(None)
            return x
        elif index + 1 == self.size():  # Removing at the tail
            x = current.getData()
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
            return x
        else:  #Removing in the middle of the list
            x = current.getData()
            previous.setNext(current.getNext())
            current.getNext().setPrevious(previous)
            return x

    def search(self, item):
        current = self.head
        found = False
        while(current != None and not(found)):
            if(current.getData() == item):
                found = True
            else:
                current = current.getNext()
        return found

    def python_list(self):
        orderList = []
        current = self.head
        while(current != None):
            orderList.append(current.getData())
            current = current.getNext()
        return orderList

    def python_list_reversed(self):  # returns a reversed list representation of the ordered list
        return self._python_list_reversed(self.head)

    def _python_list_reversed(self, start):  # helps the above function
        if start == None:
            return []
        else:
            current = start
            current.setNext(start.getNext())
            lst = self._python_list_reversed(current.getNext())
            lst.append(start.getData())
            return lst

    def size(self):
        current = self.head
        sizeList = 0
        while(current != None):
            sizeList += 1
            current = current.getNext()
        return sizeList
