# Hayden Tam
# CPE 202-Project5
import unittest
from graph import *


class TestList(unittest.TestCase):

    # def test_add_vertex(self):
    #     graph = Graph()
    #     graph.add_vertex('a')
    #     graph.add_vertex('b')
    #     self.assertEqual(graph.num_vertices, 2)
    #     graph.add_vertex('c')
    #     self.assertEqual(graph.num_vertices, 3)
    #     self.assertEqual(graph.add_vertex('d').id, Vertex('d').id)

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [
                         ['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.bicolor())

    def test_02(self):
        e = Graph('test2.txt')
        self.assertEqual(e.conn_components(), [
                         ['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(e.bicolor())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [
                         ['v1', 'v2', 'v3', 'v4']])
        self.assertTrue(g.bicolor())

    def test_04(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), ([[1, 2, 3]]))
        self.assertFalse(g.bicolor())

    def test_05(self):
        g = Graph('test5.txt')
        self.assertEqual(g.conn_components(),
                         ([['v1', 'v2', 'v3', 'v4'], ['v5']]))
        self.assertTrue(g.bicolor())

    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(),
                         ([['v1', 'v2', 'v4'], ['v3', 'v7'], ['v5']]))
        self.assertFalse(g.bicolor())

    def test_07(self):
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(),
                         ([['v1'], ['v2'], ['v3']]))
        self.assertTrue(g.bicolor())

    def test_08(self):
        g = Graph('test8.txt')
        self.assertEqual(g.conn_components(),
                         ([['v1', 'v10', 'v2', 'v3'], ['v6', 'v7', 'v8']]))
        self.assertFalse(g.bicolor())

    def test_09(self):
        g = Graph('test9.txt')
        self.assertEqual(g.conn_components(),
                         ([]))
        self.assertFalse(g.bicolor())


if __name__ == '__main__':
    unittest.main()
