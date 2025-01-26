#Write a program that reads a line of input as a string and print
#the string, with all vowels replaced by an underscore

#userInput = input("Enter a string: ")
#outputString = ""
#for ch in userInput:
#   if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#       outputString += "_"
#   else:
#       outputString += ch

userInput = input("Enter a string: ")
outputString = ""

for ch in userInput:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        outputString += "_"
    else:
        outputString += ch

print(outputString)