# Name:
# Section: 

# must use iteration not recursion
def max_list_iter(tlist):  
   """ finds the max of a list of numbers and returns it, not the index"""
   if (len(tlist) == 0):
       raise ValueError('empty list')
   """ finds the max of a list of numbers and returns it, not the index"""
   elif (len(tlist) == 1):
       return tlist[0]
   else:
       templist = tlist[1:len(tlist)]
       temp= max_list_iter(templist)
       return (max(tlist[0],temp))

#must use recursion
def reverse_rec(tempstr):   
   """ recursively reverses a list and returns it """


# Binary Search
#write your recursive binary search code here
def bin_search(target, low, high, list_val):  
   """ searches for target in list_val[low..high] and returns index if found"""
   

