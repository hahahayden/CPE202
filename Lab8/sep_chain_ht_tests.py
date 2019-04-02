# Hayden Tam
# Einakian CPE-202 Lab 8

import unittest

from sep_chain_ht import *

# Takes no parameters but for easier testing use 5 as size


class test_expressions(unittest.TestCase):
    def test_insert(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        self.assertEqual(x.hashTable, [[], [], [(2, "dog")], [], []])
        x.insert(2, "sup")
        x.insert(2, "sup")
        self.assertEqual(x.hashTable, [[], [], [(2, "sup")], [], []])
        x.insert(7, "here")  # mod 5 is 2
        self.assertEqual(
            x.hashTable, [[], [], [(2, "sup"), (7, "here")], [], []])
        # test rehash
        y = MyHashTable(2)
        y.insert(1, "dog")
        y.insert(0, "cat")
        y.insert(3, "dog")
        self.assertEqual(
            y.hashTable, [[(0, "cat")], [(1, "dog")], [], [(3, "dog")], []])
        y.insert(3, "see")
        self.assertEqual(
            y.hashTable, [[(0, "cat")], [(1, "dog")], [], [(3, "see")], []])

    def test_get(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        self.assertEqual(x.get(2), (2, "dog"))
        x.insert(7, "CAT")
        print(x.hashTable)
        self.assertEqual(x.get(2), (2, "dog"))
        x.insert(9, "sup")
        self.assertEqual(x.get(9), (9, "sup"))
        self.assertEqual(x.size(), 3)

        try:
            x.get(1)
            self.fail()
        except LookupError as e:
            self.assertEqual(
                str(e), "No key value pair.")

    def test_remove(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        self.assertEqual(x.remove(2), (2, "dog"))
        self.assertEqual(x.hashTable, [[], [], [], [], []])
        self.assertEqual(x.size(), 0)

        x.insert(2, "dog")
        x.insert(7, "cat")
        self.assertEqual(x.remove(2), (2, "dog"))
        self.assertEqual(x.hashTable, [[], [], [(7, "cat")], [], []])
        self.assertEqual(x.remove(7), (7, "cat"))
        try:
            x.remove(1)
            self.fail()
        except LookupError as e:
            self.assertEqual(
                str(e), "No key value pair.")

    def test_size(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        x.insert(2, "dog")
        x.insert(7, "cat")
        self.assertEqual(x.size(), 2)
        x.insert(9, "dog")
        self.assertEqual(x.size(), 3)
        x.insert(4, "whoa")
        self.assertEqual(x.size(), 4)
        self.assertEqual(
            x.hashTable, [[], [], [(2, "dog"), (7, "cat")], [], [(9, "dog"), (4, "whoa")]])

        y = MyHashTable(2)
        y.insert(1, "dog")

        y.insert(0, "cat")
        #self.assertEqual(x.get_table_size(), 2)
        y.insert(3, "dog")
        self.assertEqual(y.size(), 3)

    def testgettablesize(self):
        x = MyHashTable(2)
        x.insert(1, "dog")

        x.insert(0, "cat")
        self.assertEqual(x.get_table_size(), 2)
        x.insert(3, "dog")
        self.assertEqual(x.get_table_size(), 5)  # rehash
        self.assertEqual(x.hashTable, [[(0, "cat")], [
                         (1, "dog")], [], [(3, "dog")], []])

    def load_factor(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        x.insert(2, "dog")
        x.insert(7, "cat")
        self.assertEqual(x.load_factor(), 0.6)
        x.insert(9, "here")
        self.assertEqual(x.load_factor(), 0.8)

    def testCollisions(self):
        x = MyHashTable(5)
        x.insert(2, "dog")
        x.insert(2, "here")
        self.assertEqual(x.collisions(), 0)  # DOESN'T UPDATE IF SAME KEY
        x.insert(7, "cat")

        self.assertEqual(x.collisions(), 1)

        y = MyHashTable(2)
        y.insert(1, "dog")
        y.insert(0, "cat")
        y.insert(3, "dog")
        self.assertEqual(y.collisions(), 0)  # Rehash
        y.insert(4, "sup")
        self.assertEqual(y.collisions(), 0)  # REHASH

        self.assertEqual(y.get_table_size(), 5)
        y.insert(8, "whee")
        self.assertEqual(y.collisions(), 1)
        y.insert(8, "sup")
        # same key already in there so no collision just an update
        self.assertEqual(y.collisions(), 1)


if __name__ == "__main__":
    unittest.main()
