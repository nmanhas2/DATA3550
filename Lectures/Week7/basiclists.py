#you can have multiple types within a list in Python
my_number_list = [32, 54, 67.5, 29, [35, 80], "apple", 44.5, 100, 65.6]
print(my_number_list[5])

#accessing elements within a list
values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65]
values[9] = 87
print(values[9])

#list traversal
values = [2,2,3,4,5,6,7,8,9,10]
for i in range(10):
    print(i, values[i])

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
for i in range(1, 8, 2) :
   print(numbers[i], end=" ")

#reversing a list
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])

