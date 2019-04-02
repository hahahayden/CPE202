# Create a node class that has the attributes of left child, right child, and key value
# Also have helper functions that allow access to maximum value, minimum value, inserting nodes, deleting nodes, and searching


class TreeNode:
    # Purpose: to initialize the attributes key left and right
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    # Purpose: to insert a key in a specific place through recursion; setter method
    # Signature: int-> bool

    def insertNode(self, key, data=None):
        ''' For inserting the key in the Tree '''

        if key < self.key:
            ''' key less than the root key is placed to the left '''
            if self.left:
                return self.left .insertNode(key)
            else:
                self.left = TreeNode(key)

        else:
            ''' key greater than the root key is placed to the right '''
            if self.right:
                return self.right.insertNode(key)
            else:
                self.right = TreeNode(key)
    # Purpose: delete the given node setter method
    # Signature: int-> TreeNode

    def deleteNode(self, key):

        if self is None:
            return None

        # if current node's key is less than that of root node, go to the left
        if key < self.key and self.left is not None:
            self.left = self.left.deleteNode(key)
        # current node is greater than that of root node, go to the right
        elif key > self.key and self.right is not None:
            self.right = self.right.deleteNode(key)
        else:
            # deleting node with one
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # deleting node with two  chilren
            # get the minimum value successor from the right

            temp = self.minValueNode(self.right)
            self.key = temp.key
            self.right = self.right.deleteNode(temp.key)

        return self

    # Purpose: search for the key and return False or True if found; getter method
    # Signature: int-> bool

    def searchNode(self, node, key):
        if (node is None):
            return False
        if (node.key == key):
            return True
        return self.searchNode(node.right, key) or self.searchNode(node.left, key)

    # Purpose: find the minimum node within the tree; getter method
    # Signature: Node-> Node

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    # Purpose: find the maximum node witin the tree; getter method
    # Signature: Node->Node
    def maxValueNode(self, currentNode):
        if (currentNode.right):
            return self.maxValueNode(self.right)
        else:
            return currentNode

    # Purpose: to put the list inorder traverse; gettter
    # Signature: list-> list
    def inorder(self, listStr):

        if self:
            if self.left:
                self.left.inorder(listStr)
            listStr.append(int(self.key))
            listStr.append(" ")

            if self.right:
                self.right.inorder(listStr)
            return listStr

    # Purpose: to put the list in preorder traverse' getter method
    # Signature: list->list
    def preorder(self, listStr):
        '''For preorder traversal of the BST '''
        if self:
            listStr.append(int(self.key))
            listStr.append(" ")
            if self.left:
                self.left.preorder(listStr)
            if self.right:
                self.right.preorder(listStr)
            return listStr
    '''
    def findHeight(self):
        count=0
        count2=0
        while self.right != None:
            self = self.right
            count = count +1
        
        while self.left!=None:
            print('hi')
            self=self.left
            count2=count2+1
        if count2> count:
            return count2
        elif count2<count:
            return count
        elif count2==count:
            return count
        
    '''
    # Purpose: find height of the tree; count the edges; getter method
    # Signature: Node->int

    def findHeight(self, currentNode):
        if currentNode is None:
            return 0
        else:
            return max(self.findHeight(currentNode.left)+1, self.findHeight(currentNode.right)+1)

# Design Recipe: Create a binary search tree with the attribute of a root and from there having the functions of insert, delete, search, max, min, and tree traversal

#left = 0
#right = 0


class BinarySearchTree:
    # Initialize binary search tree attribute root
    def __init__(self):
        self.root = None
        self.leftCount = 0
        self.rightCount = 0
    # Purpose: check if the tree is empty by chccking the root
    # Signature: NOne-> bool

    def is_empty(self):
        if self.root == None:
            return True
        return False

    # Purpose: insert a new node at the right place on the tree; call on the helper function in node class
    # Signature: int-> Node

    def insert(self, key):
        if self.root:
            return self.root.insertNode(key)
        else:
            self.root = TreeNode(key)  # if none create root
            return self.root
    # Purpose: delete a specific node on the tree; call on the helper function in node class
    # Signature: int->Node

    def delete(self, key):
        if self.root is not None:
            return self.root.deleteNode(key)

    # Purpose: search for the specific node
    # Signature: int-> bool
    def search(self, key):
        if self.root:
            return self.root.searchNode(self.root, key)
        else:
            return False

    # Purpose: returns node with min key in the BST - can assume at least one node in BST
    # Signature: None-> Node
    def find_min(self):
        return (self.root.left.minValueNode(self.root))
    # Purpose:  returns node with max key in the BST - can assume at least one node in BST
    # Signature: NOne ->Node

    def find_max(self):
        return self.root.right.maxValueNode(self.root)

    # Purpose:  return Python list of BST keys representing preorder traversal of BST
    # Signature: none-> list of int
    def inorder_list(self):
        if self.root is not None:
            listStr = []
            listStr = self.root.inorder(listStr)

            listStr = listStr[:-1]
            newList = []
            for i in range(len(listStr)):
                if listStr[i] != " ":
                    newList.append(listStr[i])
            # print(newList)
            #listStr = "".join(listStr)
            #listStr = (listStr.split())
            return newList
    # Purpose:  return Python list of BST keys representing preorder traversal of BST
    # Signature: NOne->list of int

    def preorder_list(self):
        if self.root is not None:
            listStr = []

            listStr = self.root.preorder(listStr)
            listStr = listStr[:-1]
            newList = []
            for i in range(len(listStr)):
                if listStr[i] != " ":
                    newList.append(listStr[i])

            #listStr = "".join((listStr))
            #listStr = listStr.split()

            return newList
    # Purpose: return height of the tree
    # Signature: None->int
    '''
    def height(self):

        if self.root:
            return self.root.findHeight(self.root) - 1
        else:
            return 0
    '''

    def tree_height(self):
        if self.root == None:
            return None
        return self.tree_height_helper(self.root)

    def tree_height_helper(self, node):
        #global left
        #global right
        if node.left is not None:
            #self.leftCount = self.leftCount+1
            left = self.tree_height_helper(node.left)+1
            return left
        else:
            left = 0
            # return self.leftCount
            #left = 0
        if node.right is not None:
            right = self.tree_height_helper(node.right)+1
            #self.rightCount = self.rightCount+1
            return right
        else:
            #right = 0
            right = 0
        # return self.tree_height_helper(node.left) or self.tree_height_helper(node.right)
        return max(left, right)


tree = BinarySearchTree()
tree.insert(25)
tree.insert(15)

tree.insert(50)

tree.insert(10)
tree.insert(20)
tree.insert(3)
tree.insert(1)
tree.preorder_list()
print(tree.tree_height())
