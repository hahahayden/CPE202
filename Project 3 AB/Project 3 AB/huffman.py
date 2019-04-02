# Name: Hayden Tam and Aaron Teh
# Section: 04

# HuffmanNode is a object of class Node to represent a Huffman node created for a letter when encoding a text file
# Char is an item type String, representing the character held in the Huffman Node
# Freq is an item type Int, representing the frequency of the letter in the string held in the Huffman Node
# Left is an item type Huffman Node, representing the left child of the Huffman Node
# Right is an item type Huffman Node, representing the right child of the Huffman Node
class HuffmanNode:
      def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
            self.parent = None
      
      # Prord helper function to help find the preord string for a huffman tree
      # Self, String -> Str
      def preord(self, listStr):

        if self:
            if self.left is None and self.right is None:
                listStr.append([1, self.char])

                listStr.append(" ")
            else:
                listStr.append(0)
            if self.left:

                self.left.preord(listStr)
            if self.right:
                self.right.preord(listStr)
            return listStr
# Builds the Huffman Tree list with the list of frequencies returned from cnt_freq function
# List -> List
def buildHuffTreeList(listFrequencies):  # take in the list from cnt_freq
      case = [0]*256
      listOfNode = []
      if listFrequencies == case:
            return listOfNode
      for i in range(len(listFrequencies)):
            if(listFrequencies[i] > 0):
                  itemFreq = listFrequencies[i]  # takes the frequency number
                  itemChar = chr(i)  # takes the character
                  node = HuffmanNode(itemChar, itemFreq)
                  listOfNode.append(node)
      #             print(itemChar, itemFreq)
      # print(listOfNode)
      return listOfNode


"""returns true if tree rooted at node a comes before tree rooted at node b """

# Checks if Node A comes before Node B, returns True if it does, false if it doesn't
# Node, Node -> Bool
def comes_before(a, b):
      if a.freq < b.freq:
            return True
      elif a.freq == b.freq:
            if ord(a.char) < ord(b.char):
                  return True
            else:
                  return False
      else:
            return False

# Finds the bottom 2 child Nodes from the list of Nodes given in a form of tuple
# List -> Tuple(Node,Node)
def findMin(listOfNode):  # takes listofNode
      if listOfNode == []:
            return None,None
      minIndex = 0
      minIndex2 = 1
      for i in range(1, len(listOfNode), 1):
            # print(listOfNode[minIndex])
            # print(listOfNode[i].char)
            # (comes_before(listOfNode[minIndex], listOfNode[i]) is True) and
            if(comes_before(listOfNode[minIndex2], listOfNode[i]) is False):
                  # print('hi')
                  minIndex2 = i
            if (comes_before(listOfNode[minIndex], listOfNode[i]) is False):
                  # print('here')
                  minIndex2 = minIndex
                  minIndex = i
            if (comes_before(listOfNode[minIndex],listOfNode[minIndex2])is False):
                  # print('sup')
                  temp=minIndex2
                  minIndex2=minIndex
                  minIndex=temp
                
            # elif (comes_before(listOfNode[minIndex], listOfNode[i]) is False) and (comes_before(listOfNode[minIndex2], listOfNode[i]) is False):
                  # print('h')
                  # if (listOfNode[minIndex].freq == listOfNode[i].freq):
                  # print('hey')
                  # minIndex2 = i
      # print(listOfNode[minIndex].char, listOfNode[minIndex2].char)
      return listOfNode[minIndex], listOfNode[minIndex2]

# """ creates a new huffman node with children a and b with combined freq with name of the left child """
# # a<b

# Creates a huffman node by adding frequencies of A and B and taking the smaller ASCII value letter to make as a parent node
# Node, Node -> Node
def combine(a, b):
      if a is None and b is None:
            return None
      combineFreq = a.freq+b.freq
      # print(combineFreq)
      lowestChar = chr(min(ord(a.char), ord(b.char)))
      parentNode = HuffmanNode(lowestChar, combineFreq)
      # print(parentNode.freq, parentNode.char)
      if comes_before(a, b):
            parentNode.left = a
            parentNode.right = b
      else:
            parentNode.right = a
            parentNode.left = b
      # print(parentNode.left.char, parentNode.right.char)
      return parentNode
      # Creates a list with size 256 to hold frequency of characters in index(ord)
      # File -> List

# Takes in the filename, opens the file and makes the frequency list of size 256 to hold the frequency of the characters
# String -> List
def cnt_freq(filename):
      listFake = [0]*256
      # f = open('c:/Users/Hayden/Documents/temp/Project3/file1.txt', 'r')
      f = open(filename,'r')
      g = f.readlines()
      f.close()
      if g == []:
            return listFake
      # print('g',g)
      for x in range(len(g)):
            for i in range(len(g[x])):
                  listFake[ord(g[x][i])] += 1


      return listFake

# Creates a liss of nodes to represent the Huffman Tree
# List -> List
def create_huff_tree(list_of_freqs):
      case = [0]*256
      if list_of_freqs == case:
            return None 
      listOfNodes = buildHuffTreeList(list_of_freqs)
      while len(listOfNodes) != 1:  # find minimum
            twoMin = findMin(listOfNodes)
            parentNode = combine(twoMin[0], twoMin[1])
            twoMin[0].parent = parentNode
            twoMin[1].parent = parentNode
            listOfNodes.pop(listOfNodes.index(twoMin[0]))
            listOfNodes.pop(listOfNodes.index(twoMin[1]))
            listOfNodes.append(parentNode)

      if (len(listOfNodes) == 1):
            root = listOfNodes[0]
      return root

#istOfCode = [""]*256

# Creates the code to encode the file through a helper and recursion
# Node -> List
def create_code(node):
      L = ['']*256
      L = edit_code(node,'',L)
      return L

# Through recursion, takes in the node, code and list to go down the huffman tree and finding the code for every leaf in the tree
# Node, String, List -> List
def edit_code(node,code,L):
      if node.left is None and node.right is None:
            L[ord(node.char)] = code
      if node.left is not None:
            L = edit_code(node.left,code+'0',L)
      if node.right is not None:
            L = edit_code(node.right,code+'1',L)
      return L
   # while (node.right is not None) and (node.left is not None):
    #    letterindex = ord(node.char)

    # return listOfCode

# Encodes the infile and writes the output (encoded text) in the out_file
# String, String -> None
def huffman_encode(in_file, out_file):
      f = open(in_file,'r')
      w = open(out_file,'w+')
      g = f.readlines()
      if g == []:
            w.write('')
      else:
            listFake=cnt_freq(in_file)
            rootNode=create_huff_tree(listFake)
            codeList=create_code(rootNode)

      count = 0
      listFake = cnt_freq(in_file)
      for x in listFake:
            if x != 0:
                  count += 1
      if count == 1:
            for x in listFake:
                  if x != 0 and count == 1:
                        ordL = listFake.index(x)
                        freq = x
                        out = '\'{}\''.format(chr(ordL))+' ' +str(freq)
                        w.write(out)
            #   f = open('d:/Documents/CS/CPE202/Project 3/file2.txt', 'r')
      else:
            for i in range(len(g)):
                  for j in range(len(g[i])):
                        w.write(str(codeList[ord(g[i][j])]))
      f.close()
      w.close()

# Creates the Tree_preord for a given huffman tree
# HuffmanNode -> String
def tree_preord(node):
      if node is not None:
            listStr = []
            listStr = node.preord(listStr)
            listStr = listStr[:-1]
            newList = []
            for i in range(len(listStr)):
                  if listStr[i] != " ":
                        newList.append(listStr[i])

            listLeafString = ""
            for i in range(len(newList)):
                  if type(newList[i]) is list:
                  #     print('h9')
                        listLeafString += str(newList[i][0])
                        listLeafString += str(newList[i][1])
                  else:
                        listLeafString += str(newList[i])

            return listLeafString
      else:
            return ''


# Decodes and encoded huffman file with parameters of frequency list, encode file name, decode file name
# List, String, String -> None
def huffman_decode(listFake,encoded_file,decode_file):
      rootNode = create_huff_tree(listFake)
      # f = open('c:/Users/Hayden/Documents/temp/Project3/output1.txt', 'r')
      # f = open('C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project3/output1.txt', 'r')
      f = open(encoded_file,'r')
      g = str(f.readlines())
      decoded = 'decodefile'+encoded_file[6]+'.txt'
      # print(g)
      w = open(decoded,'w+')
      strChar = ""
      char = ''
      count = 0
      for x in listFake:
            if x != 0:
                  count += 1
                  char = chr(listFake.index(x))
      if count == 1:
            w.write(char*listFake[ord(char)]) 
      elif g != []:
            strChar = goDown(g, rootNode, strChar)
            w.write(strChar)
      f.close()
      w.close()

# Helper Function to go down a huffman tree to decode an encoded huffman file
# List, HuffmanNode, String -> String
def goDown(g, node, string):
      nodeRoot = node
      if node is not None:
            for i in g:
                  if (node.left is None and node.right is None):
                        nodeChar = node.char
                        string += nodeChar
                        node = nodeRoot
                  if (i == '1'):
                        node = node.right
                  elif (i == '0'):
                        node = node.left
            return string
      else:
            return ''
