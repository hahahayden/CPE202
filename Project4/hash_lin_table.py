# Hayden Tam
# Project 4/ CPE 202/ Einakian/ Session 03


# Creates a hashtable that treats collisions using linear probing
# Attributes of size, the list(hashtable), and loadCount
class HashTableLinPr():
    def __init__(self, size=251):

        self.size = size
        self.hashtable = [None]*size
        self.loadCount = 0
    # Checks if a number is a number or not, if not returns false
    # str/int/float-> bool

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    # Purpose: reads the stop file and creates a hashtable for it
    # Signature: str(fileName),-> list(hashtable)
    def read_stop(self, filename):
        try:
            f = open(filename, 'r')

            g = (f.readlines())
        except:
            raise FileNotFoundError
        # print(g)
        # print(len(g))

        # If the stop file has any of these characters, it takes care of it by putting a space in between it
        e = []
        g = [num.replace('-', ' ') for num in g]
        g = [num.replace('\'', '') for num in g]
        g = [num.replace('\\t', " ") for num in g]  # takes care of tabs
        g = [num.replace('\"', " ") for num in g]
        g = [num.replace('.', " ") for num in g]
        g = [num.replace(',', " ") for num in g]
        g = [num.replace(';', " ") for num in g]
        g = [num.replace('/', " ") for num in g]
        g = [num.replace('?', " ") for num in g]
        g = [num.replace('!', " ") for num in g]
        g = [num.replace('#', " ") for num in g]
        g = [num.replace('(', " ") for num in g]
        g = [num.replace(')', " ") for num in g]
        g = [num.replace('[', " ") for num in g]
        g = [num.replace(']', " ") for num in g]
        g = [num.replace('{', " ") for num in g]
        g = [num.replace('}', " ") for num in g]
        # print(g)
        # Takes the list that doesn't have the weird characters anymore and puts it into lowercase and strips where the spaces are
        for words in range(len(g)):
            # print(g[words])
            g[words] = g[words].lower()  # make lower case

            e.append(g[words].strip())

        # print("e",e)
        itemTrim = []
        # split white spaces, allows the dashes to become two separate words while the  apostrophe becomes one word
        for item in e:

            itemTrim.extend(item.split())
        # print("itemTrim",itemTrim)
        # print(itemTrim)

        #print('here', new_items)
        #print("here", new_items)
        # for insertLetter in range(len(e)):
        #     self.hashtable.append(e[insertLetter])
        # # print(self.hashtable)
        # z = open(
        #     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_wordsNew.txt', 'w')
        # for items in itemTrim:
        #     z.write(items)
        #     z.write("\n")
        itemTrim.sort()
        for insertWord in range(len(itemTrim)):
            self.hashtable.append(itemTrim[insertWord])

        f.close()

        return self.hashtable

    # Purpose:takes the input filename and the stop_table as an input; takes these and filters out the words that are in the stop word list
    # Then it takes these words and detects what line it is on then puts it into the hashtable using its hash values
    # Signature: str(filename), list(stop_table)->None

    def read_file(self, filename, stop_table):
        stop_table = stop_table.hashtable
        try:
            f = open(filename, "r")
        # f.split()
            c = (f.readlines())
        except:
            raise FileNotFoundError

        linesImportant = []
        new_items = []
        # lineValues = []
        # print(c)

        c = [num.replace('-', ' ') for num in c]
        c = [num.replace('\'', '') for num in c]
        c = [num.replace('\\t', " ") for num in c]  # takes care of tabs
        c = [num.replace('\"', " ") for num in c]
        c = [num.replace('.', " ") for num in c]
        c = [num.replace(',', " ") for num in c]
        c = [num.replace(';', " ") for num in c]
        c = [num.replace('/', " ") for num in c]
        c = [num.replace('?', " ") for num in c]
        c = [num.replace('!', " ") for num in c]
        c = [num.replace('#', " ") for num in c]
        c = [num.replace('(', " ") for num in c]
        c = [num.replace(')', " ") for num in c]
        c = [num.replace('[', " ") for num in c]
        c = [num.replace(']', " ") for num in c]
        c = [num.replace('{', " ") for num in c]
        c = [num.replace('}', " ") for num in c]

        for words in range(len(c)):
            c[words] = c[words].lower()
            c[words] = c[words].strip()
            linesImportant.append(c[words])

        #print("lines important", linesImportant)
        # split white spaces\
        itemTrim = []
        for item in linesImportant:

            new_items.extend(item.split())
        #print("here", new_items)
        # newNewList = new_items[:]
        # print('new_items', new_items)
        for item in range(len(linesImportant)):
            itemTrim.append(linesImportant[item].split())
        #print("itemTrim", itemTrim)
        newNewList = []
        # takes away the ones in stop
        for k in range(len(new_items)):
            if (new_items[k] not in stop_table):
                if (new_items[k]not in newNewList):
                    if(self.is_number(new_items[k]) is False):

                        newNewList.append(new_items[k])
        # print(newNewList)
        # print(len(newNewList))
        lineValues = []*len(newNewList)
        # print(lineValues)
        newNewList.sort()
        #print('newnew', newNewList)
        finalValues = []
        # Creates a sublist within the list to include the key and the item( the line value)
        for i in range(len(newNewList)):
            # print(newNewList[i])

            for j in range(len(itemTrim)):
                for k in range(len(itemTrim[j])):
                    if (newNewList[i] == itemTrim[j][k]):

                        lineValues.append((newNewList[i], j+1))
        newWord = None
        for i in range(len(lineValues)):
            if (list(lineValues[i]) not in finalValues):
                finalValues.append([lineValues[i][0], lineValues[i][1]])

           # else:
        group = []

        indexValue = 0
        for i in range(len(finalValues)):

            if finalValues[i][0] == newWord:

                group[indexValue].append(finalValues[i][1])

            else:
                group.append([finalValues[i][0], finalValues[i][1]])
                newWord = finalValues[i][0]
                indexValue = i

        # Inserts the word into the hashtable using the my_hash function
        # Rehash when needed

        for insertWord in range(len(group)):
            # if the load factor is less than .75 it is efficeint if not rehash
            if self.get_load_fact() >= .75 or self.myhash(group[insertWord][0], self.size) >= self.size:

                table_size = self.reHash(self.size)
                self.size = table_size
            # Continues after rehashing the values that were already within the hashtable
            index = self.myhash(group[insertWord][0], self.size)

            self.hashtable[index] = (
                group[insertWord])
            self.loadCount += 1
            '''
            if self.loadCount/self.size >= .75:  # or h_valueTotal >= self.size:

                table_size = self.reHash(self.size)
                self.size = table_size
            '''

    # Helper function that helps get all the values within the hashtable, since global lists aren't allowed
    # None-> list
    def get_all_elements(self):
        list_of_elements = []
        #print("hash", self.hashtable)
        for element in self.hashtable:
            if(element != None):
                list_of_elements.append(element)
        list_of_elements.sort()
        # print(list_of_elements)
        return list_of_elements
        # return
    # Gets the size of the table
    # None-> int

    def get_tablesize(self):
        return self.size()

    # Writes the values into a output file by getting the index and taking the key and item and putting it into an output file
    # Signature: str(output file)->None
    def save_concordance(self, output_filename):
        linesImportant = self.get_all_elements()
        f = open(output_filename, "w+")
        # minus one when gettign value cuz will detect a double
        # print(linesImportant)
        for items in range(len(linesImportant)):
            # print(items)
            # print(self.hashtable.index(self.linesImportant[items]))

            placement = self.myhash(linesImportant[items][0], self.size)

            #print("placement", placement)
            # print(index)

            f.write(str(self.hashtable[placement][0]))
            f.write(":")
            f.write("\t")
            # "{:<15}".format("     ")
            # f.write(str(self.hashtable[placement][1]))

            # f.write(str("\n"))
            #print("last", self.hashtable)
            for length in range(1, len(self.hashtable[placement])):

                f.write(str(self.hashtable[placement][length]))
                if (len(self.hashtable[placement]) > 2) and length+1 != len(self.hashtable[placement]):

                    f.write(" ")

            if (items != len(linesImportant)-1):
                f.write('\r')
                f.write("\n")
        # f.strip()
        f.close()

    # Purpose: get the load factor
    # Signature: None-> Int
    def get_load_fact(self):
        # items /size
        # print('here2', len(self.linesImportant))
        return (self.loadCount)/self.size

    # Hash the values in; if the value is taken within the hashtable linear probe by increasing index by one
    # Signature: string, list-> int
    def myhash(self, key, table_size):
        h_value = []
        h_valueTotal = 0
        # print(key)
        '''
        for i in range(len(key)):
            if (len(key) >= 8):
                exponentValue = 8-1-8  # if greater than 8 jsut use 8
        '''
        # up to length 8 and takes the index till 8
        for i in range(min(len(key), 8)):

            exponentValue = len(key)-1-i
            h_value.append(((ord(key[i])*31**(exponentValue))))
        # print(h_value)

        for values in range(len(h_value)):
            h_valueTotal += h_value[values]
            h_valueTotal = round(h_valueTotal % table_size)
        # print(h_valueTotal)
        # test values???
        #print("uhoh", h_valueTotal, key)
        # and self.hashtable[h_valueTotal][0] != key
        while h_valueTotal < table_size and self.hashtable[h_valueTotal] is not None and self.hashtable[h_valueTotal][0] != key:

            #print("lienar probing")

            # print(self.hashtable)
            h_valueTotal += 1
        # or h_valueTotal >= self.size:

        # self.hashtable[h_valueTotal] = key
        return h_valueTotal

    # IF the load factor is greater than .75 rehash the table by creating a table 2*size +1 and then put the values that are already in it again
    # List-> int
    def reHash(self, table_size):
        newSize = 2*table_size+1
        # for words in range(len(self.linesImportant):
        self.size = newSize
        values = self.get_all_elements()
        #print("hey", self.valuesImportant)
        self.hashtable = [None]*self.size
        for things in range(len(values)):
            #print('reHash', things, self.size)
            #print("linesRehash:", values[things])
            index = self.myhash(values[things][0], self.size)

            self.hashtable[index] = (
                values[things])
            print("here:", values[things], index)
        return self.size


stopWordHash = HashTableLinPr(500)
stopWordHash.read_stop(
    'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
fileWordHash = HashTableLinPr(6)

fileWordHash.read_file(
    'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input3.txt', stopWordHash)
# print("done")
# # print(fileWordHash.hashtable)
fileWordHash.save_concordance(
    'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput3.txt')
# # hash.myhash("cat", 6)
# # print(hash.myhash("ca", 6))
# # print(hash.myhash("dg", 6))
# # print(hash.myhash("dog", 6))
# # print(hash.myhash("doggie", 6))
# # print(hash.size)
# # print(hash.hashtable)
# # hash.myhash("cat", 251)
# # print(hash.hashtable)

# # hash = LinearHashing(251)
# # ash.fileWordHash.


# stopWordHash = HashTableLinPr(500)
# stopWordHash.read_stop(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
# print(stopWordHash.hashtable)
# fileWordHash = HashTableLinPr(2)

# fileWordHash.read_file(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input1.txt', stopWordHash)

# # print(fileWordHash.hashtable)
# fileWordHash.save_concordance(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput1.txt')
# print(fileWordHash.size)
# print(fileWordHash.loadCount)

# # print(fileWordHash.hashtable)
# stopWordHash = HashTableLinPr(500)
# stopWordHash.read_stop(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
# print(stopWordHash.hashtable)
# fileWordHash = HashTableLinPr()

# fileWordHash.read_file(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input2.txt', stopWordHash)
# # print(fileWordHash.hashtable)

# fileWordHash.save_concordance(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput2.txt')
# print(fileWordHash.hashtable)
