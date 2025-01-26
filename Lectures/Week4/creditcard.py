#Here is a loop that builds a new string
#containing a credit card # with spaces
#and dashes removed:

userInput = input("Enter a credit card number: ")

creditCardNumber = ""

for char in userInput:
    if(char != " " and char != "-"):
        creditCardNumber += char

print(creditCardNumber)