import random

def linear_search_dy(list, target) :
    for i in range(len(list)) :
        if list[i] == target :
            return i
    return -1

def randomlist(n):
    list = []
    for i in range (n):
        list.append(random.randrange(0,n))
    return list

list = randomlist(int(input("How many numbers in the list: ")))
target = int(input("which number are you look for: "))
print(linear_search_dy(list, target))
print(list)