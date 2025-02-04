#5. Write a program that reads a five-digit posititve integer and breaks it into a sequence of 
#   individual digits.
#   Ex: 16384 would give 1 6 3 8 4

userInput = input("Enter a five-digit positive integer: ")

fiveDigitInt = str(userInput)

print("%s %s %s %s %s" % (fiveDigitInt[0], fiveDigitInt[1], fiveDigitInt[2], fiveDigitInt[3], 
                          fiveDigitInt[4]))