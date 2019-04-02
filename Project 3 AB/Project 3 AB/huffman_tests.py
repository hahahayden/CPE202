# Name: Hayden Tam and Aaron Teh
# Section: 04

import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
      
      # Test for 'ddddddddddddddddccccccccbbbbaaff'
      def test_cnt_freq(self):
            freqlist = cnt_freq("file1.txt")
            anslist = [0]*256
            anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
            self.assertListEqual(freqlist[97:104], anslist[97:104])
      def test_create_huff_tree(self):
            freqlist = cnt_freq("file1.txt")
            hufftree = create_huff_tree(freqlist)
            numchars = 32
            charforroot = "a"
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(ord(hufftree.char), 97)
            left = hufftree.left
            self.assertEqual(left.freq, 16)
            self.assertEqual(ord(left.char), 97)
            right = hufftree.right
            self.assertEqual(right.freq, 16)
            self.assertEqual(ord(right.char), 100)
      def test_create_code(self):
            freqlist = cnt_freq("file1.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('d')], '1')
            self.assertEqual(codes[ord('a')], '0000')
            self.assertEqual(codes[ord('f')], '0001')
      def test_01_encodefile(self):
            huffman_encode("file1.txt", "output1.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output1.txt", "answer1.txt"))
      def test_tree_preord(self):
            tree = create_huff_tree(cnt_freq('file1.txt'))
            self.assertEqual(tree_preord(tree),'00001a1f1b1c1d')
      def test_01_decodefile(self):
            freqlist = cnt_freq("file1.txt")
            huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))

      # Test for 'ddacefef'
      def test_cnt_freq1(self):
            freqlist2 = cnt_freq("file2.txt")
            anslist = [0]*256
            anslist[97:104] = [1, 0, 1, 2, 2, 2, 0] 
            self.assertListEqual(freqlist2[97:104], anslist[97:104])
      def test_create_huff_tree1(self):
            freqlist2 = cnt_freq("file2.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 8
            charforroot = "a"
            self.assertEqual(hufftree2.freq, 8)
            self.assertEqual(ord(hufftree2.char), 97)
            left = hufftree2.left
            self.assertEqual(left.freq, 4)
            self.assertEqual(ord(left.char), 97)
            right = hufftree2.right
            self.assertEqual(right.freq, 4)
            self.assertEqual(ord(right.char), 101)
      def test_create_code1(self):
            freqlist = cnt_freq("file2.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('a')], '000')
            self.assertEqual(codes[ord('c')], '001')
            self.assertEqual(codes[ord('d')], '01')
            self.assertEqual(codes[ord('e')], '10')
            self.assertEqual(codes[ord('f')], '11')
      def test_01_encodefile1(self):
            huffman_encode("file2.txt", "output2.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output2.txt", "answer2.txt"))
      def test_tree_preord1(self):
            tree = create_huff_tree(cnt_freq('file2.txt'))
            self.assertEqual(tree_preord(tree),'0001a1c1d01e1f')
      def test_01_decodefile1(self):
            freqlist = cnt_freq("file2.txt")
            huffman_decode(freqlist,"output2.txt", "decodefile2.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile2.txt", "file2.txt")) 

      # Test for 'abcd abc ab a'
      def test_cnt_freq2(self):
            freqlist2 = cnt_freq("file3.txt")
            anslist = [0]*256
            anslist[97:104] = [4, 3, 2, 1, 0, 0, 0] 
            self.assertListEqual(freqlist2[97:104], anslist[97:104])
            self.assertListEqual(freqlist2[32:33],[3])
      def test_create_huff_tree2(self):
            freqlist2 = cnt_freq("file3.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 8
            charforroot = " "
            self.assertEqual(hufftree2.freq, 13)
            self.assertEqual(ord(hufftree2.char), 32)
            left = hufftree2.left
            self.assertEqual(left.freq, 6)
            self.assertEqual(ord(left.char), 32)
            right = hufftree2.right
            self.assertEqual(right.freq, 7)
            self.assertEqual(ord(right.char), 97)  
      def test_create_code2(self):
            freqlist = cnt_freq("file3.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord(' ')], '00')
            self.assertEqual(codes[ord('a')], '11')
            self.assertEqual(codes[ord('b')], '01')
            self.assertEqual(codes[ord('c')], '101')
            self.assertEqual(codes[ord('d')], '100')
      def test_01_encodefile2(self):
            huffman_encode("file3.txt", "output3.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output3.txt", "answer3.txt"))
      def test_tree_preord2(self):
            tree = create_huff_tree(cnt_freq('file3.txt'))
            self.assertEqual(tree_preord(tree),'001 1b001d1c1a')
      def test_01_decodefile2(self):
            freqlist = cnt_freq("file3.txt")
            huffman_decode(freqlist,"output3.txt", "decodefile3.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile3.txt", "file3.txt")) 

      # Test for 'bbbbbbbbb'
      def test_cnt_freq3(self):
            freqlist2 = cnt_freq("file7.txt")
            anslist = [0]*256
            anslist[97:104] = [0, 9, 0, 0, 0, 0, 0] 
            self.assertListEqual(freqlist2[97:104], anslist[97:104])
      def test_create_huff_tree3(self):
            freqlist2 = cnt_freq("file7.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 8
            charforroot = " "
            self.assertEqual(hufftree2.freq, 9)
            self.assertEqual(ord(hufftree2.char), 98)
            # left = hufftree2.left
            # self.assertEqual(left.freq, None)
            # self.assertEqual(ord(left.char), None)
            # right = hufftree2.right
            # self.assertEqual(right.freq, None)
            # self.assertEqual(ord(right.char), None)     
      def test_create_code3(self):
            freqlist = cnt_freq("file7.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('b')], '')
      def test_01_encodefile3(self):
            huffman_encode("file7.txt", "output7.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output7.txt", "answer7.txt"))
      def test_tree_preord3(self):
            tree = create_huff_tree(cnt_freq('file7.txt'))
            self.assertEqual(tree_preord(tree),'1b')
      def test_01_decodefile3(self):
            freqlist = cnt_freq("file7.txt")
            huffman_decode(freqlist,"output7.txt", "decodefile7.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile7.txt", "file7.txt")) 

      # Test for 'This is a test for huffman coding'
      def test_cnt_freq4(self):
            freqlist2 = cnt_freq("file8.txt")
            anslist = [0]*256
            anslist[97:117] = [2, 0, 1, 1, 1, 3, 1,2,3,0,0,0,1,1,1,0,0,1,3,2,1] 
            self.assertListEqual(freqlist2[97:104], anslist[97:104])
            self.assertListEqual(freqlist2[32:33],[6])
            self.assertListEqual(freqlist2[84:85],[1])
      def test_create_huff_tree4(self):
            freqlist2 = cnt_freq("file8.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 8
            charforroot = " "
            self.assertEqual(hufftree2.freq, 33)
            self.assertEqual(ord(hufftree2.char), 32)
            left = hufftree2.left
            self.assertEqual(left.freq, 14)
            self.assertEqual(ord(left.char), 84)
            right = hufftree2.right
            self.assertEqual(right.freq, 19)
            self.assertEqual(ord(right.char), 32)     
      def test_create_code4(self):
            freqlist = cnt_freq("file8.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('a')], '0101')
            self.assertEqual(codes[ord(' ')], '111')
            self.assertEqual(codes[ord('i')], '000')
      def test_01_encodefile4(self):
            huffman_encode("file8.txt", "output8.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output8.txt", "answer8.txt"))
      def test_tree_preord4(self):
            tree = create_huff_tree(cnt_freq('file8.txt'))
            self.assertEqual(tree_preord(tree),'0001i1s0001T1c1a001d1e01g1m0001h1n01o01r1u001t1f1 ')
      def test_01_decodefile4(self):
            freqlist = cnt_freq("file8.txt")
            huffman_decode(freqlist,"output8.txt", "decodefile8.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile8.txt", "file8.txt"))

      # Test for 's'
      def test_cnt_freq5(self):
            freqlist2 = cnt_freq("file6.txt")
            self.assertListEqual(freqlist2[115:116],[1])
      def test_create_huff_tree5(self):
            freqlist2 = cnt_freq("file6.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 1
            charforroot = "s"
            self.assertEqual(hufftree2.freq, 1)
            self.assertEqual(ord(hufftree2.char), 115)
            # did not test left or right because single char does not have left or right child
      def test_create_code5(self):
            freqlist = cnt_freq("file6.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('s')], '')
      def test_01_encodefile5(self):
            huffman_encode("file6.txt", "output6.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output6.txt", "answer6.txt")) 
      def test_tree_preord5(self):
            tree = create_huff_tree(cnt_freq('file6.txt'))
            self.assertEqual(tree_preord(tree),'1s')
      def test_01_decodefile5(self):
            freqlist = cnt_freq("file6.txt")
            huffman_decode(freqlist,"output6.txt", "decodefile6.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile6.txt", "file6.txt"))

      # Test for empty file
      def test_cnt_freq6(self):
            freqlist2 = cnt_freq("file5.txt")
            anslist = [0]*256
            anslist[97:104] = [0,0,0,0,0,0,0] 
            self.assertListEqual(freqlist2[97:104], anslist[97:104])
      def test_create_huff_tree6(self):
            freqlist2 = cnt_freq("file5.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 1
            charforroot = ""
            self.assertEqual(hufftree2, None)
            # did not test left or right because single char does not have left or right child
      # did not test create tree because no huffman tree for empty file
      # did not test create code because empty file does not have code
      def test_01_encodefile6(self):
            huffman_encode("file5.txt", "output5.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output5.txt", "answer5.txt"))
      def test_tree_preord6(self):
            tree = create_huff_tree(cnt_freq('file5.txt'))
            self.assertEqual(tree_preord(tree),'')
      def test_01_decodefile6(self):
            freqlist = cnt_freq("file5.txt")
            huffman_decode(freqlist,"output5.txt", "decodefile5.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile5.txt", "file5.txt"))

      #test for h\ne\nl\nl\no
      def test_cnt_freq7(self):
            freqlist = cnt_freq('file4.txt')
            anslist = [0]*256
            anslist[100:109] = [0,1,0,0,1,0,0,0,2]
            self.assertTrue(freqlist[100:109],anslist[100:109])
            self.assertTrue(freqlist[111],1)
            self.assertTrue(freqlist[10],4)
      def test_create_huff_tree7(self):
            freqlist2 = cnt_freq("file4.txt")
            hufftree2 = create_huff_tree(freqlist2)
            numchars = 5
            charforroot = "\n"
            self.assertEqual(hufftree2.freq, 9)
            self.assertEqual(ord(hufftree2.char), 10)
            # did not test left or right because single char does not have left or right child
      def test_create_code7(self):
            freqlist = cnt_freq("file4.txt")
            hufftree = create_huff_tree(freqlist)
            codes = create_code(hufftree)
            self.assertEqual(codes[ord('h')], '1111')
            self.assertEqual(codes[ord('e')], '1110')
            self.assertEqual(codes[ord('l')], '10')
            self.assertEqual(codes[ord('o')], '110')
            self.assertEqual(codes[ord('\n')], '0')
      def test_01_encodefile7(self):
            huffman_encode("file4.txt", "output4.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("output4.txt", "answer4.txt")) 
      ''' Cannot test tree_preord for multiple lines'''
      # def test_tree_preord7(self):
      #       tree = create_huff_tree(cnt_freq('file4.txt'))
      #       copy = tree
      #       while copy.char != None:
      #             print(copy.char)
      #             copy = copy.left
      #       self.assertEqual(tree_preord(tree),'01\n01101o01e1h')
      def test_01_decodefile7(self):
            freqlist = cnt_freq("file4.txt")
            huffman_decode(freqlist,"output4.txt", "decodefile4.txt")
            # capture errors by running 'filecmp' on your encoded file
            # with a *known* solution file
            self.assertTrue(filecmp.cmp("decodefile4.txt", "file4.txt"))


      # Test find min
      def test_find_min(self):
            L = [HuffmanNode('a',14),HuffmanNode('c',6),HuffmanNode(' ',3),HuffmanNode('g',7),HuffmanNode('d',2)]
            A = findMin(L)
            self.assertEqual((A[0].char,A[1].char),(HuffmanNode('d',2).char,HuffmanNode(' ',3).char))
if __name__ == '__main__': 
   unittest.main()
