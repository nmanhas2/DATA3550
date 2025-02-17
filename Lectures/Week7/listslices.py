#different options for slicing
even_numbers = [0, 2, 4, 6, 8, 10]
print(even_numbers[2:4])
print(even_numbers[:3])
print(even_numbers[3:])
print(even_numbers[:])

#you can slice with strings
greeting = "Hello World!"
print(greeting[3:8])

#you can cast a list onto a range as well
dong_list = list(range(1, 21))
print(dong_list)

#looking at a part of a list, ie. grabbing the third quarter of temperatures
temperatures = [18, 21, 24, 28, 33, 39, 40, 39, 36, 30, 22, 18]
thirdQuarter = temperatures[6 : 9]

print(thirdQuarter)

#you can also replace using slices as well
temperatures = [18, 21, 24, 28, 33, 39, 40, 39, 36, 30, 22, 18]

temperatures[6 : 9] = [450, 440, 400]

print(temperatures[ : ])

#the size of the slice also doesn't have to match the replacement
#this essentially replaces the first two elements, then adds another
#element to the list entirely

names = ["Fred", "Ann", "Sue", "betsy"]
names[ : 2] = ["Peter", "Paul", "Mary"]

print(names)

#you can extract a sublist or sub-string with slicing as well
greeting = "Hello, World!"
greeted = greeting[7 : 12]   # The substring "World"

print(greeted[ : ])

#there's also negative indexing
#remember that -1 is the last element
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[-1])
print(numbers[-2:])
print(numbers[:-3])