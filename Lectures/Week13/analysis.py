##
#  This program measures how long it takes to sort a list of a
#  user-specified size with the selection sort algorithm.
#

from random import randint
from time import time

def bubble_sort(list):
    def swap(i, j):
        list[i], list[j] = list[j], list[i]

    n = len(list)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if list[i - 1] > list[i]:
                swap(i - 1, i)
                swapped = True

    return list

def selection_sort(list):
    for i in range(len(list)):
        minimum = i

        for j in range(i + 1, len(list)):
            # Select the smallest value
            if list[j] < list[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        list[minimum], list[i] = list[i], list[minimum]

    return list

def insertion_sort(list) :
    for i in range(1, len(list)):
        j = i
        while list[j-1] > list[j] and j > 0 :
          list[j -1]  , list[j] = list[j], list[j-1]
          j-= 1

def merge_sort(list):

     # a list of 0 or one elment is sorted, by definition.
    if len(list) <= 1:
        return list

    if len(list) > 1:
        left_list = list[ :len(list)//2]
        right_list = list[len(list)//2:]

        # recursion
        merge_sort(left_list)
        merge_sort(right_list)

        #merge
        i = 0 # i is the left most index of the left list
        j = 0 # j is the left most indes of the right list
        k = 0 # merged list index
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k += 1
            else:
                list[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
             list[k] = left_list[i]
             i += 1
             k += 1

        while j < len(right_list):
             list[k] = right_list[j]
             j += 1
             k += 1

def quick_sort(list):
    if len(list)> 1:
        pivot=list.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in list:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quick_sort(smlr_lst) + equal_lst + quick_sort(grtr_lst))
    else:
        return list

firstSize = int(input("Enter first list size: "))
numberOfLists = int(input("Enter number of lists: "))

for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   v = []

   # Construct random list.
   for i in range(size) :
      v.append(randint(1, 100))

   startTime = time()
   bubble_sort(v)
   endTime = time()

   print("Size: %d Elapsed time for bubble Sort Algorithm: %.3f seconds" % (size, endTime - startTime))

print('__________')


for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   v1 = []

   # Construct random list.
   for i in range(size) :
      v1.append(randint(1, 100))

   startTime = time()
   selection_sort(v1)
   endTime = time()

   print("Size: %d Elapsed time for Selection Sort Algorithm: %.3f seconds" % (size, endTime - startTime))

print('__________')


for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   v2 = []

   # Construct random list.
   for i in range(size) :
      v2.append(randint(1, 100))

   startTime = time()
   insertion_sort(v2)
   endTime = time()

   print("Size: %d Elapsed time for Insertion Sort Algorithm: %.3f seconds" % (size, endTime - startTime))

print('__________')


for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   v3 = []

   # Construct random list.
   for i in range(size) :
      v3.append(randint(1, 100))

   startTime = time()
   merge_sort(v3)
   endTime = time()

   print("Size: %d Elapsed time for Merge Sort Algorithm: %.3f seconds" % (size, endTime - startTime))

print('__________')


for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   v4 = []

   # Construct random list.
   for i in range(size) :
      v4.append(randint(1, 100))

   startTime = time()
   merge_sort(v4)
   endTime = time()

   print("Size: %d Elapsed time for Quick Sort Algorithm: %.3f seconds" % (size, endTime - startTime))