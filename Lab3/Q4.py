#Factoring of integers. Write a program that asks the user 
#for an integer and then prints out all its prime factors

valid = False

while not valid:
    userInput = input("Enter an integer: ")
    number = abs(int(userInput))
    if number == 0 or number == 1:
        print("Error! Enter an integer other than 1.")
    else:
        factor = 2
        while number > 1:
            while number % factor == 0:
                print(factor, end=", ")
                number = number // factor
            factor += 1
        valid = True