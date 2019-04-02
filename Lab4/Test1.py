class Node:
    def __init__(self, itemData):
        self.data = itemData
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

    def getPrevious(self):
        return self.previous

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __repr__(self):
        print(self.head)

    def is_empty(self):
        if(self.head is None):
            return True
        else:
            return False

    def add(self, item):
        currentNode = self.head

        previousNode = None
        stopLoop = False
        while((currentNode != None) and not(stopLoop)):
            # if(currentNode.getData() > item):
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
            temp.setNext(self.head)
            # self.head.setPrevious(temp)
            self.head = temp.previous
            self.head = temp

            self.num_items += 1
        # If the item to be added has to be at the end
        elif(currentNode == None):
            # temp.setPrevious(self.tail)
            temp.previous = self.tail
            # self.tail.setNext(temp)
            self.tail.next = temp
            self.tail = temp
            self.num_items += 1

        # If the item to be added has to be in th middle
        else:
            # temp.setNext(currentNode)
            temp.next = currentNode
            # temp.setPrevious(previousNode)
            temp.prev = previousNode
            # previousNode.setNext(temp)
            previousNode.next = temp
            # currentNode.setPrevious(temp)
            currentNode.prev = temp
            self.num_items += 1

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
        if(previous == None):
            self.head = current.next
            self.num_items -= 1
            # self.head.setPrevious(None)
            self.head.prev = None
        # Removing item at the end
        elif(current.getNext() == None):
            self.num_items -= 1
            #self.tail = self.tail.getPrevious()
            self.tail = self.tail.previous
            # self.tail.setNext(None)
            self.tail.next = None
        # Removing in the middle
        else:
            # previous.setNext(current.getNext())
            previous.next = current.next
            # current.getNext().setPrevious(previous) RIGHT???????
            # current.next.previous=previous
            current.next = previous
            self.num_items -= 1
        return count

    def search_forward(self, item):

        current = self.head
        found = False
        while(current != None and not(found)):
            if(current.data == item):
                found = True
            else:
                current = current.next
        return found

    def search_backward(self, item):
        current = self.tail
        found = False
        while(current != None and not(found)):
            if(current.data == item):

                found = True
            else:
                current = current.previous
                # print(current.data)
        return found

    def size(self):
        return self.num_items

    def index(self, item):
        current = self.head
        index = 0
        while(current != None):
            if(current.data == item):
                return index
            else:
                index += 1
                current = current.next
        return None

    def pop(self):
        current = self.head
        # Removing at the tail
        x = current.data
        self.tail = self.tail.previous
        # self.tail.setNext(None)
        self.tail.next = None
        return x

    def pop(self, index):

        current = self.head
        previous = None
        if index < 0 or index > self.size():
            raise IndexError
        for i in range(index):
            previous = current
            current = current.getNext()

        if index == 0:  # Removing at the head
            x = current.getData()
            self.head = self.head.getNext()
            self.head.setPrevious(None)
            return x

        else:  # Removing in the middle of the list
            x = current.getData()
            previous.setNext(current.getNext())
            current.getNext().setPrevious(previous)
            return x


x = OrderedList()
x.add(20)


x.add(2)

x.add(5)

x.add(1)
x.add(0)
x.add(24)
x.add(60)
x.add(100)
print(x.head.data)
print(x.head.data)
print(x.tail.data)
print(x.num_items)
print(x.remove(100))
print(x.remove(60))
print(x.remove(1))
print(x.head.data)
print(x.pop())
print(x.tail.data)
