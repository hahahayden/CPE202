#Hayden Tam
#Project 4/ CPE 202/ Einakian/ Session 03
#Quadratic Probing

#Creates a hashtable that treats collisions using quadratic probing
#Attributes of size, the list(hashtable), and loadCount
class HashTableQuadPr():
    def __init__(self, size=251):

        self.size = size
        self.hashtable = [None]*size
        self.loadCount = 0
     #Checks if a number is a number or not, if not returns false
    #str/int/float-> bool
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
     #Purpose: reads the stop file and creates a hashtable for it
    #Signature: str(fileName),-> list(hashtable)
    def read_stop(self, filename):
        try:
            f = open(filename, 'r')

            g = (f.readlines())
        except:
            raise FileNotFoundError
        # print(g)
        # print(len(g))
        #If the stop file has any of these characters, it takes care of it by putting a space in between it
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
        for words in range(len(g)):
            # print(g[words])
            g[words] = g[words].lower()  # make lower case

            e.append(g[words].strip())

        # print("lines important", linesImportant)
        # split white spaces\
        itemTrim = []
        #split white spaces, allows the dashes to become two separate words while the  apostrophe becomes one word
        for item in e:

            itemTrim.extend(item.split())
        #print(itemTrim)

       
        itemTrim.sort()
        for insertWord in range(len(itemTrim)):
            self.hashtable.append(itemTrim[insertWord])

        f.close()

        return self.hashtable

    #Purpose:takes the input filename and the stop_table as an input; takes these and filters out the words that are in the stop word list
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
        # #print(c)
        d = []
        # for items in range(len(c)):
            # print("here", c)
            # print(d)
        new = c[:]
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
        # print('c', c)
        g = []
        for it in range(len(c)):
            c[it] = c[it].lower()
            c[it] = c[it].strip()
            g.append(c[it])

        # print(g)

        for words in range(len(new)):
            new[words] = new[words].lower()
            new[words] = new[words].strip()
            linesImportant.append(new[words])

        # print("lines important", linesImportant)
        # split white spaces\
        itemTrim = []
        for item in linesImportant:

            new_items.extend(item.split())
        
        d = []
        for stuff in range(len(new_items)):
            if (new_items[stuff] not in stop_table):
                d.append(new_items[stuff])
        # print('d', d)
        putIntoStringAgain = ""
        for i in d:
            putIntoStringAgain += i
            putIntoStringAgain += " "
        # print(putIntoStringAgain)
        putIntoStringAgain = putIntoStringAgain.split()
        # print('hey', putIntoStringAgain)
        d = [num.replace('-', ' ')
             for num in d]
        d = [num.replace('\'', '') for num in d]
        d = [num.replace('\\t', " ") for num in d]  # takes care of tabs
        d = [num.replace('\"', " ") for num in d]
        d = [num.replace('.', " ") for num in d]
        d = [num.replace(',', " ") for num in d]
        d = [num.replace(';', " ") for num in d]
        d = [num.replace('/', " ") for num in d]
        d = [num.replace('?', " ") for num in d]
        d = [num.replace('!', " ") for num in d]
        d = [num.replace('#', " ") for num in d]
        d = [num.replace('(', " ") for num in d]
        d = [num.replace(')', " ") for num in d]
        d = [num.replace('[', " ") for num in d]
        d = [num.replace(']', " ") for num in d]
        d = [num.replace('{', " ") for num in d]
        d = [num.replace('}', " ") for num in d]

        # print(d)

        # print(d)
        e = []
        for stuff in range(len(d)):
            splitted = d[stuff].split()
            for item2 in splitted:
                e.append(item2)
        # print(e)

        # GOOOOOD!

        for item in range(len(g)):
            itemTrim.append(g[item].split())
        # print("itemTrim", itemTrim)
        newNewList = []
        # print(new_items)
        # takes away the ones in stop

        for k in range(len(e)):
            if (e[k] not in stop_table):
                if (e[k]not in newNewList):
                    if(self.is_number(e[k]) is False):

                        newNewList.append(e[k])

 
        lineValues = []*len(newNewList)
        # #print(lineValues)
        newNewList.sort()
      
        finalValues = []
     
        for i in range(len(newNewList)):
            # #print(newNewList[i])

            for j in range(len(itemTrim)):
                for k in range(len(itemTrim[j])):
                    if (newNewList[i] == itemTrim[j][k]):
                        # #print(index)
                        # #print(newNewList)
                        lineValues.append((newNewList[i], j+1))
                        # if (newNewList[])

        # #print("final values", lineValues)
        newWord = None
        for i in range(len(lineValues)):
            if (list(lineValues[i]) not in finalValues):
                finalValues.append([lineValues[i][0], lineValues[i][1]])
 
        group = []
        

        indexValue = 0
        for i in range(len(finalValues)):

            if finalValues[i][0] == newWord:

                group[indexValue].append(finalValues[i][1])

            else:
                group.append([finalValues[i][0], finalValues[i][1]])
                newWord = finalValues[i][0]
                indexValue = i

        for insertWord in range(len(group)):

            if self.get_load_fact() >= .75 or self.myhash(group[insertWord][0], self.size) >= self.size:

                table_size = self.reHash(self.size)
                self.size = table_size

            index = self.myhash(group[insertWord][0], self.size)

            self.hashtable[index] = (
                group[insertWord])
            self.loadCount += 1

    #Helper function that helps get all the values within the hashtable, since global lists aren't allowed
    # None-> list
    def get_all_elements(self):
        list_of_elements = []
        # #print("hash", self.hashtable)
        for element in self.hashtable:
            if(element != None):
                list_of_elements.append(element)
        list_of_elements.sort()
       # #print(list_of_elements)
        return list_of_elements
        

    #Gets the tablesize of the hashtable
    #None-> int
    def get_tablesize(self):
        return self.size()

      #Writes the values into a output file by getting the index and taking the key and item and putting it into an output file
    # Signature: str(output file)->None
    def save_concordance(self, output_filename):
        linesImportant = self.get_all_elements()
        f = open(output_filename, "w+")
        # minus one when gettign value cuz will detect a double
        # #print(linesImportant)
        for items in range(len(linesImportant)):
        

            placement = self.myhash(linesImportant[items][0], self.size)

            f.write(str(self.hashtable[placement][0]))
            f.write(":")
            f.write("\t")
       


            for length in range(1, len(self.hashtable[placement])):

                f.write(str(self.hashtable[placement][length]))
                if (len(self.hashtable[placement]) > 2) and length+1 != len(self.hashtable[placement]):

                    f.write(" ")

            if (items != len(linesImportant)-1):
                f.write("\r")
                f.write("\n")
        # f.strip()
        f.close()

    #Purpose: get the load factor
    # Signature: None-> Int

    def get_load_fact(self):

        return (self.loadCount)/self.size

    #Hash the values in; if the value is taken within the hashtable quadratic probe by increasing index to square it to by one if colliosn
    #Signature: string, list-> int
    def myhash(self, key, table_size):
        num = 0
        h_value = []
        h_valueTotal = 0
        # #print(key)

        for i in range(len(key)):
            if (len(key) >= 8):
                exponentValue = 8-1-i  # if greater than 8 jsut use 8
            else:
                exponentValue = len(key)-1-i
            h_value.append(((ord(key[i])*31**(exponentValue))))
        # #print(h_value)

        for values in range(len(h_value)):
            h_valueTotal += h_value[values]
            h_valueTotal = round(h_valueTotal % table_size)

        while h_valueTotal < table_size and self.hashtable[h_valueTotal] is not None and self.hashtable[h_valueTotal][0] != key:


            h_valueTotal = h_valueTotal + num**2

            num += 1

        return h_valueTotal
    
    #IF the load factor is greater than .75 rehash the table by creating a table 2*size +1 and then put the values that are already in it again
    #List-> int
    def reHash(self, table_size):
        newSize = 2*table_size+1
        # for words in range(len(self.linesImportant):
        self.size = newSize
        values = self.get_all_elements()
        # #print("hey", self.valuesImportant)
        self.hashtable = [None]*self.size
        for things in range(len(values)):
            # #print('reHash', things, self.size)
           # #print("linesRehash:", values[things])
            index = self.myhash(values[things][0], self.size)

            self.hashtable[index] = (
                values[things])
            # #print("here:", values[things], index)
        return self.size


# stopWordHash = HashTableQuadPr(500)
# stopWordHash.read_stop(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
# fileWordHash = HashTableQuadPr(6)

# fileWordHash.read_file(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input3.txt', stopWordHash)
# #print("done")
# # # #print(fileWordHash.hashtable)
# fileWordHash.save_concordance(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput3.txt')
# hash.myhash("cat", 6)
# #print(hash.myhash("ca", 6))
# #print(hash.myhash("dg", 6))
# #print(hash.myhash("dog", 6))
# #print(hash.myhash("doggie", 6))
# #print(hash.size)
# #print(hash.hashtable)
# hash.myhash("cat", 251)
# #print(hash.hashtable)

# hash = LinearHashing(251)
# ash.fileWordHash.


# stopWordHash = HashTableQuadPr(500)
# stopWordHash.read_stop(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
# # #print(stopWordHash.hashtable)
# fileWordHash = HashTableQuadPr(251)

# fileWordHash.read_file(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input1.txt', stopWordHash)

# # # #print(fileWordHash.hashtable)
# fileWordHash.save_concordance(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput1.txt')
# # print(fileWordHash.size)
# # print(fileWordHash.loadCount)


# stopWordHash = HashTableQuadPr(500)
# stopWordHash.read_stop(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/stop_words.txt')
# # #print(stopWordHash.hashtable)
# fileWordHash = HashTableQuadPr()

# fileWordHash.read_file(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/input2.txt', stopWordHash)
# # #print(fileWordHash.hashtable)

# fileWordHash.save_concordance(
#     'C:/Users/hayde/OneDrive - California Polytechnic State University/CPE202/Project 4/myoutput2.txt')
# # #print(fileWordHash.hashtable)
