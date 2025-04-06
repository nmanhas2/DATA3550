##
#  This program measures how long it takes to sort a list of a
#  user-specified size with the selection sort algorithm.
#

from random import randint
from time import time

def mergeSort(arr):
    if len(arr) > 1:
       mid = len(arr)//2
       L = arr[:mid]
       R = arr[mid:]
       print(f"L:{L}")
       print(f"R:{R}")
       mergeSort(L)
       mergeSort(R)

       i = j = k = 0

       while i < len(L) and j < len(R):
            print(f"first while {L} : {L[i]} | {R} : {R[j]}")
            
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(f"first while: k: {k} j:{j} i:{i}")

       while i < len(L):
            arr[k] = L[i]
            print(f"second while arr: {arr} {arr[k]} {L[i]}")           
            i += 1
            k += 1
            print(f"second while: k: {k} j:{j} i:{i}")

       while j < len(R):
            print(f"third while arr: {arr} {arr[k]} {R[j]}")
            arr[k] = R[j]
            j += 1
            k += 1
            print(f"third while: k: {k} j:{j} i:{i}")
       print(f"arr: {arr}")

firstSize = int(input("Enter first list size: "))
numberOfLists = int(input("Enter number of lists: "))

for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   values = []
   # Construct random list.
   for i in range(size) :
      values.append(randint(1, 100))
   print(values)
   startTime = time()
   mergeSort(values)
   endTime = time()
   print(values)
   print("Size: %d Elapsed time: %.3f seconds" % (size, endTime - startTime))