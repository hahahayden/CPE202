# Hayden Tam
# CPE202-03
# Project 5
# Sussan Einakian
# class Vertex creates a vertex and has the attributes of adjacent to and id
# Also has functions that adds the neighbor into the adjacency list and has a str function to represent the attributes


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        # self.adjacent_to = []
        self.adjacent_to = []
        # self.visited = False
        # self.color = 'none'

    # Helper to add neighbor vertex
    # int,string-> None
    def addNeighbor(self, key, weight=0):
        self.adjacent_to.append(key)

    # String to represent attributes
    # None-> string
    def __str__(self):
        return str(self.id) + ' adjacent_to: ' + str([x.id for x in self.adjacent_to])


# Graph has the attributes of the vertices list and the number of vertices inserted
# Also has functions to add vertex, get vertex, add edge, and create connected components and determine bipartitie or not
class Graph:
    def __init__(self, filename):

        #self.connections = []
        try:
            f = open(filename, "r")
        except:
            raise FileNotFoundError
        lines = [line.rstrip('\n') for line in f]
        self.vertList = {}
        self.numVertices = 0
        pairs = lines[0:]

        pairsList = []

        for items in range(len(pairs)):
            pairsList.append(pairs[items].split())
        print("pairsList", pairsList)

        #self.keys = lines[:]

        item = []

        for key1 in range(len(pairsList)):
            if len(pairsList[key1]) > 1:

                if pairsList[key1][0] not in item and pairsList[key1][0] not in self.vertList:
                    self.add_vertex(pairsList[key1][0])

                    # print("here", pairsList[key1][1])
                    item.append(pairsList[key1][0])

                if pairsList[key1][1] not in item and pairsList[key1][1] not in self.vertList:
                    self.add_vertex(pairsList[key1][1])

                self.add_edge(pairsList[key1][0], pairsList[key1][1])
            else:
                self.add_vertex(pairsList[key1][0])
                #self.add_edge(pairsList[key1][0], pairsList[key1][0])
        f.close()

    # Purpose; to add a vertex into the dictionary list of self.vertList
    # int/str-> Vertex
    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # Purose: to get the vertex designated
    # int/str-> Vertex/NOne
    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None

    # Purpose: add edges between nodes; connect them
    # Vertex,Vertex-> none
    def add_edge(self, v1, v2):
        if v1 not in self.vertList:
            nv = self.add_vertex(v1)
        if v2 not in self.vertList:
            nv = self.add_vertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2])
        self.vertList[v2].addNeighbor(self.vertList[v1])

    # Purpose: helps the depth first search to connect components
    # Vertex,list,list->list

    def depthRecursion(self, vertex, visited, componentList):
        visited.append(self.vertList[vertex].id)
        componentList.append(self.vertList[vertex].id)
        listKeys = self.vertList[vertex].adjacent_to
        print(listKeys)
        for key in listKeys:
            if(not(key.id in visited)):
                self.depthRecursion(key.id, visited, componentList)
        componentList.sort()
        return componentList

 # Returns a list of connected components inside the graph
 # None ---> Graph
    def conn_components(self):
        visitedList = []
        componentList = []
        listKeys = self.vertList.keys()
        connectedComponent = []

        for key in listKeys:
            if(not(key in visitedList)):

                componentList.append(self.depthRecursion(
                    key, visitedList, connectedComponent))
                connectedComponent = []

        componentList.sort()
        for items in range(len(componentList)):
            for item2 in range(len(componentList[items])):
                print('here', item2)

                if self.is_number(componentList[items][item2]):
                    componentList[items][item2] = int(
                        componentList[items][item2])
        for x in range(len(componentList)):
            componentList[x].sort()

        return componentList

     # Purpose: to determine if a graph is bipartite or not
    # None-> bool

    def bicolor(self):
        listKeys = self.vertList.keys()
        if len(listKeys) == 0:  # empty file false because not even a graph
            return False
        for key in listKeys:
            a = []
            b = []
            a.append(key)

            for connection in self.vertList[key].adjacent_to:
                b.append(connection.id)
            for connection in self.vertList[key].adjacent_to:
                for nextconnection in connection.adjacent_to:
                    if(nextconnection.id in b):
                        return False
                    else:
                        if(nextconnection.id not in a):
                            a.append(nextconnection.id)
        return True

    # Purpose; tests if the input is a num or not
    # str,float,int-> bool
    def is_number(self, s):
        try:

            float(s)
            return True
        except ValueError:
            return False

    # Gets the vertices within the dictionary vertList
    # None-> list
    def get_vertices(self):
        return list(self.vertList.keys())

    # String representation of the vertex and connections
    # None-> Str
    def __str__(self):
        return "\n".join([str(self.get_vertex(x).__str__()) for x in self.vertList])


# x = Graph("C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project5/Given/test5.txt")
# # x = Graph('test5.txt')

# print(x.conn_components())

# # print(x.numVertices)
# # print(x.__str__())
# # print(len(x.vertList['v1'].adjacent_to))
# print(x.bicolor())
