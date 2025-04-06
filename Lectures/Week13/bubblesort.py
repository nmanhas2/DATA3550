# Python program for implementation of Bubble Sort
from random import randint
from time import time
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
           return

##
#  This program measures how long it takes to sort a list of a
#  user-specified size with the selection sort algorithm.
#

firstSize = int(input("Enter first list size: "))
numberOfLists = int(input("Enter number of lists: "))

for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   values = []
   # Construct random list.
   for i in range(size) :
      values.append(randint(1, 100))

   startTime = time()
   bubbleSort(values)
   endTime = time()

   print("Size: %d Elapsed time: %.3f seconds" % (size, endTime - startTime))