#Write a program that computesd the number of years 
#required to triple the initial balance. User inputs
#initial balance (positive) and the rate (positive)

continueApp = "Y"

while continueApp == "Y":

    initialBalance = float(input("Enter initial balance: "))
    if initialBalance <= 0:
        print("Sorry, I didn't understand that. The balance should be positive.")
        break

    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Sorry, I didn't understand that. The rate should be positive.")
        break

    years = 0
    currentBalance = initialBalance
    tripleBalance = initialBalance * 3

    while currentBalance < tripleBalance:
        interest = currentBalance * rate / 100
        currentBalance = currentBalance + interest
        years += 1

    print("With an initial balance of $%.2f, the investment will be tripled after %d years at a rate of %.2f %" % (initialBalance, years, rate))
    
    continueApp = input("Would you like to do more investment calculations (Y/N)?: ")




