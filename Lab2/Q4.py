#Write a program whose inputs are three
#integers, and whose ouput is the smallest
#of the three values

inputOne = int(input("Enter an integer (#1): "))
inputTwo = int(input("Enter an integer (#2): "))
inputThree = int(input("Enter an integer (#3): "))

if inputOne < inputTwo and inputOne < inputThree:
    print(inputOne)
elif inputTwo < inputOne and inputTwo < inputThree:
    print(inputTwo)
else:
    print(inputThree)
    