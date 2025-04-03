from random import randint
## Sorts a list, using selection sort.

def selectionSort(values) :
   for i in range(len(values)) :
      minPos = minimumPosition(values, i)
      temp = values[minPos]  # swap the two elements
      values[minPos] = values[i]
      values[i] = temp

def minimumPosition(values, start) :
   minPos = start
   for i in range(start + 1, len(values)) :
      if values[i] < values[minPos] :
         minPos = i

   return minPos

n = 20
values = []
for i in range(n) :
   values.append(randint(1, 100))
print(values)
selectionSort(values)
print(values)