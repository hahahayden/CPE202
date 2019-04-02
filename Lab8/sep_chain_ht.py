# Hayden Tam
# Einakian CPE-202 Lab 8

# Create a hashtable that deals with collisions by chaining; if hash value the same it appends it to the end of the index
# Functions: able to insert key values into the hash table, get value, and remove the key
# Attributes: the hashtable has the attributes of number of items within the hashtable, and the number of collisions


class MyHashTable():

    def __init__(self, table_size=11):
        self.hashTable = [[] for _ in range(table_size)]
        #self.startSize = table_size
        self.num_items = 0
        self.num_collisions = 0
    # Insert the key into the hashtable using the hashvvalue as the index
    # int,string/float/int-> None

    def insert(self, key, item):
        if(key < 0):
            print("Negative number not allowed")
        else:
            hashValue = key % self.get_table_size()
            twin = False
            if(self.hashTable[hashValue] == []):
                self.hashTable[hashValue].append((key, item))
                self.num_items += 1
            else:
                # go through the hashtable's index to insert if the value already there
                # if the key is the same replace it
                for index in range(len(self.hashTable[hashValue])):
                    if(self.hashTable[hashValue][index][0] == key):
                        self.hashTable[hashValue][index] = (key, item)
                       # self.hashTable[hashValue].insert(0, (key, item))
                        twin = True
                        #self.num_collisions += 1
                # if the key is not the same, append to teh end of the sublist
                # so no twin because the duplicate key isn't there
                if((twin) is False and self.load_factor() < 1.5):
                    self.hashTable[hashValue].append((key, item))
                    self.num_items += 1
                    self.num_collisions += 1
                print(self.hashTable)
                # if the factor is greater than 1.5, rehash for more efficient list

                if(self.load_factor() >= 1.5):
                    print("rehash")
                    oldTable = self.hashTable
                    newHashTable = [[]
                                    for _ in range((self.get_table_size()*2)+1)]
                    self.hashTable = newHashTable
                    self.num_items = 0
                    # reset collisions when hit rehash
                    self.num_collisions = 0
                    for item in oldTable:
                        for keypair in item:
                            self.insert(keypair[0], keypair[1])
    # Purpose: get the size of the table
    # None-> int

    def get_table_size(self):
        return len(self.hashTable)

    # Purpose: Use the key value to find the destination and return the key and the item within that hashed index

    # Signature: int-> tuple
    def get(self, key):
        hashValue = key % self.get_table_size()
        # get the value for easy indexing
        for index in range(len(self.hashTable[hashValue])):
            if(key == self.hashTable[hashValue][index][0]):
                #self.num_items -= 1
                return self.hashTable[hashValue][index]
        raise LookupError("No key value pair.")
    # Purpose: remove a key from the hashtable
    # Signature: int-> tuple

    def remove(self, key):
        hashValue = key % self.get_table_size()
        for index in range(len(self.hashTable[hashValue])):
            if(key == self.hashTable[hashValue][index][0]):
                self.num_items -= 1
                return self.hashTable[hashValue].pop(index)
        raise LookupError("No key value pair.")

    # Purpose: size of the amount of insertions; the amount of (key,item) within the hashtable
    # Signature: None-> int
    def size(self):
        return self.num_items
    # Purpose: get the load factor of the hashtable; number of insertions/ table size
    # signature: None-> float

    def load_factor(self):
        #print("start", self.startSize)
        print("size:", self.size())
        return self.size()/self.get_table_size()
    # Purpose: get the number of collisions  happened
    # Signature: none-> int

    def collisions(self):
        return self.num_collisions

        # x = MyHashTable(4)
        # x.get_table_size()
        # x.insert(16, "cat")
        # x.insert(18, "odg")
        # x.insert(21, "here")
        # x.insert(26, "sup")
        # x.insert(29, "sup")
        # x.insert(29, "heloo")
        # x.insert(15, "heloo")
        # x.insert(2, "heloo")
        # print(x.hashTable)
