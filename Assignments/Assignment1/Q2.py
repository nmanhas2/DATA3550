#You are given 4 floating-point numbers. Use a string formatting expression with 
#conversion specifiers to
#output their product and their average as integers (rounded) and floating-point numbers.
#Output each rounded integer using the following:
#
#print('{:.0f}'.format(your_value))
#
#Output each floating-point value with three digits after the decimal point, which can 
#be achieved as follows:
#
#print('{:.3f}'.format(your_value))

def getFloatingPoint():
    while 1:
        try:

            num = float(input("Enter a floating point number: "))
            return num
        
        except ValueError as e:

            print(f"Invalid input: Error: {e}")

def printRounded(number):
    print('{:.0f}'.format(number))

def printUnrounded(number):
    print('{:.3f}'.format(number))

def main():
    total = 0
    product = 1
    myNumbers = []

    for i in range(0, 4):
        myNumbers.append(getFloatingPoint())
        num = myNumbers[i]
        total += num
        product *= num

    average = total / len(myNumbers)

    printRounded(product)
    printUnrounded(product)
    printRounded(average)
    printUnrounded(average)

main()
