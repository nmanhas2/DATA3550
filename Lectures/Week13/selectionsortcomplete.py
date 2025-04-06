#@title SelectionSort
##
#  The selectionSort function sorts a list using the selection sort algorithm.
#

def selectionSort(values) :
   for i in range(len(values)) :
      minPos = minimumPosition(values, i)
      temp = values[minPos]  # swap the two elements
      values[minPos] = values[i]
      values[i] = temp
      print(values)

## Finds the smallest element in a tail range of the list.

def minimumPosition(values, start) :
   minPos = start
   for i in range(start + 1, len(values)) :
      print(f"{values[i]} {values[minPos]}")
      if values[i] < values[minPos] :
         minPos = i
         

   return minPos

#@title SelectionDemo
from random import randint
# from selectionsort import selectionSort

n = 3
values = []
for i in range(n) :
   values.append(randint(1, 100))
print(values)
selectionSort(values)

