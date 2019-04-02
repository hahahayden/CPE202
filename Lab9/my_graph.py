# Hayden Tam
# Lab9: Connected Graphs
# Sussan Einakian Cpe 202/ 03
# Class Vertex contains attributes of id and connectionTo other vertices
# The class also has a add neighbor function to add to the connectionTo list
# Also has a string representation function to show its connections


class Vertex:

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        # self.adjacent_to = []
        self.connectedTo = {}
        #self.visited = False

    # Purpose to show the neighbors connected to the vertex
    # Sig: int-> None
    def addNeighbor(self, key, weight=0):
        self.connectedTo[key] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        # return self.connectedTo

# Class Graph has attributes of vertex List and numVertices
# Contains connect components and helper functions to retreive vertex id's and connection Lists


class MyGraph:
    def __init__(self, filename):
        self.connections = []  # adjacency list
        f = open(filename, "r")
        lines = [line.rstrip('\n') for line in f]
        self.vertList = {}
        self.numVertices = 0
        self.numOfVertices = lines[0]
        self.numOfVertices = int(self.numOfVertices)
        #
        # print(self.numOfVertices)
        pairs = lines[2:]

        pairsList = []
        connections = [[] for _ in range(self.numOfVertices)]
        for items in range(len(pairs)):
            pairsList.append(pairs[items].split())
        # print(pairsList)

        self.keys = lines[:]
        for stuff in range(len(pairsList)):
            # print(pairsList[stuff])

            connections[int(pairsList[stuff][0])-1].append(
                int(pairsList[stuff][1]))
            # connections[int(pairsList[stuff][0])].append(pairsList[stuff][1])
            print(connections)
        item = []
        self.connections = connections[:]
        #print("connections", self.connections)
        for key in range(self.numOfVertices):
            # if (len(self.connections[key]) > 0):

            self.add_vertex(int(key+1))
            #print("key", key+1)
            item.append(key+1)
        for key1 in range(len(self.connections)):
            for key2 in range(len(self.connections[key1])):
                if key2 not in item:
                    #print("here", self.connections[key1][key2])
                    self.add_vertex(int(self.connections[key1][key2]))
                    item.append(key2)
                self.add_edge(key1+1, int(self.connections[key1][key2]))

    # Adds a vertex and increasese the number of vertices
    # Signature: int -> Vertex
    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # Gets the vertex
    # Signature: int-> Vertex
    def get_vertex(self, key):
        return self.vertList[key]

    # Adds an edge to the two vertices; creates a connection
    # Vertex,Vertex-> None
    def add_edge(self, v1, v2):
        if v1 not in self.vertList:
            nv = self.add_vertex(v1)
        if v2 not in self.vertList:
            nv = self.add_vertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2])
        self.vertList[v2].addNeighbor(self.vertList[v1])

    # Helper function to get the connection of components
    # Vertex,list, list-> list
    def depthRecursion(self, vertex, visited, components):
        visited.append(self.vertList[vertex].id)
        components.append(self.vertList[vertex].id)
        # goes throught the keys in it and if its not in the visited appends it
        list_of_keys = self.vertList[vertex].connectedTo.keys()
        for key in list_of_keys:
            if(not(key.id in visited)):
                self.depthRecursion(key.id, visited, components)
        components.sort()  # sorts the vertices within that component
        return components

 # Returns a list of connected components inside the graph
 # None ---> list
    def conn_components(self):
        visitedVertices = []
        finalComponents = []
        connectedComponent = []
        list_of_keys = self.vertList.keys()
        for key in list_of_keys:
            if(not(key in visitedVertices)):
                finalComponents.append(self.depthRecursion(  # takes care of the ones connected together
                    key, visitedVertices, connectedComponent))  # splits the vertices into components
                connectedComponent = []  # set to [] to start over again for new component
        # print(finalComponents)
        return finalComponents

    def bicolor(self):
        bicolor = True
        list_of_keys = self.vertList.keys()
        for key in list_of_keys:
            u = []
            v = []
            u.append(key)
            for connection in self.vertList[key].connected_to:
                v.append(connection.id)
            for connection in self.vertList[key].connected_to:
                for aconnection in connection.connected_to:
                    if(aconnection.id in v):
                        return False
                    else:
                        if(not(aconnection.id in u)):
                            u.append(aconnection.id)
        return True


# x = MyGraph(
#     "C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/test3.txt")
# x = MyGraph('test1.txt')
# print("test1", x.conn_components())
# y = MyGraph('test2.txt')
# print("test2", y.conn_components())
# z = MyGraph('test3.txt')
# print("test3", z.conn_components())
# c = MyGraph('test4.txt')
# print("test4", c.conn_components())
# x.conn_components()
x = MyGraph(
    "C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project5/Given/test1.txt")

print(x.vertList.items())
x.conn_components()
# print(x.numVertices)
# print(x.__str__())
# print(len(x.vertList['v1'].connectedTo))
print(x.bicolor())

print(x.get_vertices())
