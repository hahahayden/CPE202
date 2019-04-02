# Start of unittest - add to completely test functions in exp_eval

import unittest
from TestBSTREE import *


class test_expressions(unittest.TestCase):
    def test_empty(self):
        tree=BinarySearchTree()
        self.assertTrue(tree.is_empty(),True)
        tree.insert(4)
        self.assertFalse(tree.is_empty(),False)
    def test_insert(self):
        tree=BinarySearchTree()
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)
        self.assertFalse(tree.is_empty(),False)
        self.assertTrue(tree.search(5),True)

    def test_search(self):
        tree=BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(10)
        tree.insert(2)
        tree.insert(4)
        self.assertTrue(tree.search(4),True)
        self.assertTrue(tree.search(2),True)
        self.assertTrue(tree.search(4),True)
        tree.delete(2)
        self.assertFalse(tree.search(2),False)
    def test_deleteroot(self):
        tree=BinarySearchTree()
        tree.insert(5)
        self.assertEqual(tree.root.key,5)
        tree.insert(3)
        tree.insert(10)
        tree.insert(20)
        tree.insert(14)
        tree.insert(2)
        tree.insert(4)
        tree.delete(5)
        self.assertEqual(tree.root.key,10)
        tree.delete(10)
        
        self.assertEqual(tree.root.key,14)
    def test_deleteOther(self):
        tree=BinarySearchTree()
        tree.insert(5)
        
        tree.insert(3)
        tree.insert(10)
        tree.insert(20)
        tree.insert(14)
        tree.insert(2)
        tree.insert(4)
        tree.delete(20)
        self.assertFalse(tree.search(20),False)
        self.assertEqual(tree.root.right.key,10)
        
        tree.delete(3)
        self.assertEqual(tree.root.left.left.key,2)
        tree.delete(4)
        self.assertEqual(tree.root.left.key,2)
    
    def test_find_min(self):
        tree=BinarySearchTree()
        tree.insert(5)
        
        tree.insert(3)
        tree.insert(10)
        tree.insert(20)
        tree.insert(14)
        tree.insert(2)
        tree.insert(4)
        self.assertEqual(tree.find_min(),2)
        tree.delete(2)
        self.assertEqual(tree.find_min(),3)
    
    def test_find_max(self):
        tree=BinarySearchTree()
        tree.insert(5)
        
        tree.insert(3)
        tree.insert(10)
        tree.insert(20)
        tree.insert(14)
        tree.insert(2)
        tree.insert(4)
        self.assertEqual(tree.find_max(),20)
        tree.delete(20)
        self.assertEqual(tree.find_max(),14)
    
    def test_inorder_list(self):
        tree=BinarySearchTree()
        tree.insert(25)
        tree.insert(15)
        tree.insert(50)
        tree.insert(10)
        tree.insert(22)
        tree.insert(35)
        tree.insert(70)


        self.assertEqual(tree.inorder_list(), "10 15 22 25 35 50 70")
        tree.insert(4)
        tree.insert(12)
        tree.insert(18)
        tree.insert(24)
        tree.insert(31)
        tree.insert(44)
        tree.insert(66)
        tree.insert(90)
        self.assertEqual(tree.inorder_list(), "4 10 12 15 18 22 24 25 31 35 44 50 66 70 90")

    def test_preorder_list(self):
        tree=BinarySearchTree()
        tree.insert(25)
        tree.insert(15)
        tree.insert(50)
        tree.insert(10)
        tree.insert(22)
        tree.insert(35)
        tree.insert(70)
        tree.insert(4)
        tree.insert(12)
        tree.insert(18)
        tree.insert(24)
        tree.insert(31)
        tree.insert(44)
        tree.insert(66)
        tree.insert(90)
        self.assertEqual(tree.preorder(), "25 15 10 4 12 22 18 24 50 35 31 44 70 66 90")

    def test_treeheight(self):
        tree=BinarySearchTree()
        self.assertEqual(tree.height(),0)
        tree.insert(25)
        tree.insert(15)
        tree.insert(50)
        tree.insert(10)
        self.assertEqual(tree.height(),2)
        tree.insert(22)
        tree.insert(35)
        tree.insert(70)
        tree.insert(4)
        tree.insert(12)
        tree.insert(18)
        tree.insert(24)
        tree.insert(31)
        tree.insert(44)
        tree.insert(66)
        tree.insert(90)
        self.assertEqual(tree.height(),3)
        tree.insert(100)
        self.assertEqual(tree.height(),4)
if __name__ == "__main__":
    unittest.main()
