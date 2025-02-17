numbers = list(range(1, 16))
print("Original list:", numbers)

print("Reversed list:", numbers[::-1])

print("Only the last 3 items:", numbers[:-4:-1])

#Ex Create a list containing the elements 1 to 20.
#Use the slicing operator to output elements at index 0-4, index 4-8 and index 8-10 of
#this list.

numbers = list(range(1,21))
print(numbers[0:5])
print(numbers[4:9])
print(numbers[8:11])