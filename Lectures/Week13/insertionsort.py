# Function to do insertion sort
from random import randint
from time import time
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        print(arr)
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                print(arr)
        arr[j+1] = key
        print(arr)

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
   insertionSort(values)
   endTime = time()

   print("Size: %d Elapsed time: %.3f seconds" % (size, endTime - startTime))