#Write a program with loops that computes the sum of all
#odd numbers between a and b, where a and b are inputs

#ask for input a, ask for input b, find the max/min of the two
#total = 0
#for num in range(min + 1, max)
#   if num is odd:
#       total += num

a = int(input("Enter a number (a): "))
b = int(input("Enter a number (b): "))

maximum = max(a, b)
minimum = min(a, b)
total = 0

for num in range(minimum, maximum + 1):
    if num % 2:
        total += num

print(total)