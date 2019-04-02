import random
import time
import sys
import copy
print(sys.getrecursionlimit())
sys.setrecursionlimit(50000)

#Purpose: sorts list using insertion sort
#List-> int
def insertion_sort(alist):
    count = 0
    for index in range(1, len(alist)):
        count+=2
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
            count += 2
        
        alist[position] = currentvalue
        count+=1
    return count

#Purpose: sorts list using selection sort
#List-> int
def selection_sort(alist):
    comparisons = 0
    startTime  = time.time()
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        comparisons+=2
        for location in range(1,fillslot+1):
            comparisons+=2
            if alist[location]>alist[positionOfMax]:
                comparisons += 1
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        comparisons+=1
    return comparisons

#Purpose: sorts using merge sort
#list-> int
def merge_sort(alist):
    count3 = 0

    if len(alist) > 1:
        count3 += 1
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
                count3 += 1
            else:
                alist[k] = righthalf[j]
                j = j+1
                count3 += 1
            k = k+1
            count3 += 2
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
            count3 += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
            count3 += 1 

    return count3


countQuick = 0

#Purpose: sorts using quick sort
#List-> int
def quickSort(alist):
  global countQuick
  quickSortHelper(alist,0,len(alist)-1)
  return(countQuick)

#Purpose: helps quick sort function by dividing list into subparts
#list, int,int-> None
def quickSortHelper(alist,first,last):
  global countQuick
  if first<last:
      countQuick+=1
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)
#Purpose: splits the list and updates to make it sorted
#List, int,int-> int
def partition(alist,first,last):
  global countQuick
  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      countQuick+=1
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          countQuick+=2
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          countQuick+=2
          rightmark = rightmark -1

      if rightmark < leftmark:
          countQuick+=1
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp
          countQuick+=1
  
  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp
  countQuick+=1
  return rightmark

#main file to call on sorted and unsorted lists and sorts
#None-> None
def main():
    
    counter = 1000
    while counter <= 32000:
        alist = random.sample(range(counter), counter)  # 10 int
    
        alist2 = alist[:]
    
        alist3 = alist[:]
        alist4 = alist[:]
        # print(alist)
        
        start_timeInsertion = time.time()
        
        print("Insertion Unsorted Comparisons",insertion_sort(alist))
        end_timeInsertion = time.time()
        sort_timeInsertion = end_timeInsertion-start_timeInsertion
        print("Insertion", counter,  sort_timeInsertion)

    
    
        start_timeSelection = time.time()
        print("Selection Unsorted Comparisons",selection_sort(alist2))
        end_timeSelection = time.time()
        sort_timeSelection = end_timeSelection-start_timeSelection

        print("Selection Unsorted", counter, sort_timeSelection)
        
        start_timeMerge = time.time()
        print("Merge Unsorted Comparisons",merge_sort(alist3))
        end_timeMerge = time.time()
        sort_timeMerge = end_timeMerge-start_timeMerge
        print("Merge", counter, sort_timeMerge)
        
        start_timeQuick = time.time()
        print("Quick Unsorted Comparisons",quickSort(alist4))
        end_timeQuick = time.time()
        sort_timeQuick = end_timeQuick-start_timeQuick
        print("Quick", counter, sort_timeQuick)
        
        counter *= 2
        
        
    
    counterSorted = 1000
    while counterSorted <= 32000:
        SortedAlist = random.sample(range(counterSorted), counterSorted)  
        SortedAlist.sort()
        
        SortedAlist2 = SortedAlist[:]

        SortedAlist3 = SortedAlist2[:]
        SortedAlist4 = SortedAlist2[:]
        
        # print(alist)
        
        start_timeInsertion = time.time()

        print("Insertion Sorted Comparisons",insertion_sort(SortedAlist))
        end_timeInsertion = time.time()
        sort_timeInsertion = end_timeInsertion-start_timeInsertion
        print("Insertion Sorted", counterSorted,  sort_timeInsertion)

        start_timeSelection = time.time()
        print("Selection Sorted Comparisons",selection_sort(SortedAlist2))
        end_timeSelection = time.time()
        sort_timeSelection = end_timeSelection-start_timeSelection

        print("Selection Sorted", counterSorted, sort_timeSelection)
        
        
        start_timeMerge = time.time()
        print("Merge Sorted Comparisons",merge_sort(SortedAlist3))
        end_timeMerge = time.time()
        sort_timeMerge = end_timeMerge-start_timeMerge
        print("Merge Sorted", counterSorted, sort_timeMerge)
    
        start_timeQuick = time.time()
        print("Quick Sorted Comparisons",quickSort(SortedAlist4))
        end_timeQuick = time.time()
        sort_timeQuick = end_timeQuick-start_timeQuick
        print("Quick Sorted", counterSorted, sort_timeQuick)
        
        counterSorted *= 2
        

#Call the main
main()