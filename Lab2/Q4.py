#Write a program whose inputs are three
#integers, and whose ouput is the smallest
#of the three values

inputOne = input("Enter an integer (#1): ")
inputTwo = input("Enter an integer (#2): ")
inputThree = input("Enter an integer (#3): ")

if(inputOne.isdigit() and inputTwo.isdigit() and inputThree.isdigit()):
    print(min(int(inputOne), int(inputTwo), int(inputThree)))
else:
    print("Please enter three integers.")

    