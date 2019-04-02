# Hayden Tam Test file for Lab 9
# Einakian CPE 202/03
import unittest
from my_graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        g = MyGraph('test1.txt')
        self.assertEqual(g.conn_components(), [
                         [1, 2, 3, 4, 5], [6, 7, 8, 9]])

    def test_02(self):
        g = MyGraph('test2.txt')
        self.assertEqual(g.conn_components(), [
                         [1, 2, 3], [4, 6, 7, 8], [5]])

    def test_03(self):
        g = MyGraph('test2.txt')
        self.assertEqual(g.conn_components(), [
                         [1, 2, 3, 10], [4], [5], [6, 7, 8], [9]])


if __name__ == '__main__':
    unittest.main()
