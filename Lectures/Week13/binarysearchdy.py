import random

def randomlist(n):
    list = []
    for i in range (n):
        list.append(random.randrange(0,n))
    return list

def binary_search_dy(list, target): # Binary search can be implemented iteratively, loops to reapeat
        first = 0
        last = len(list)-1

        while first<=last:
            #note: Use of // indicates floor division. Ex. 5//2 = 2
            midpoint = (first + last)//2
            if list[midpoint] == target:
                return midpoint
            else:
                if target < list[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return None

x = randomlist(int(input("How many numbers in the list: ")))

print(binary_search_dy(x, 4))
print(binary_search_dy(x, 30))
print(binary_search_dy(x, 57))