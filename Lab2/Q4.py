#My test case: input = -45, 45, 3923783, output was -45

inputOne = int(input("Enter an integer (#1): "))
inputTwo = int(input("Enter an integer (#2): "))
inputThree = int(input("Enter an integer (#3): "))

print(min(inputOne, inputTwo, inputThree))

#could also do it like this, if we're not allowed to use min function:
if inputOne < inputTwo and inputOne < inputThree:
  print(inputOne)
elif inputTwo < inputOne and inputTwo < inputThree:
  print(inputTwo)
else:
  print(inputThree)