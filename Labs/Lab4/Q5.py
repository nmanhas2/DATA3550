#Prompt user for an integer
#verify that it is in fact an integer, prompt again if it's not
#add it to the list
#repeat until user is done

#prompt user for lower bound
#verify that it is an integer, prompt again if not
#repeat for the upper bound
#check if the upper bound is in fact higher or equal to the lower bound, prompt if not

#check what numbers are within the bounds
#add them to the new list
#print it out once done

def intCheck(userInput):
    if userInput.replace("-","").isdigit():
        return True
    else:
        return False

def lowerBound():

    while 1:
        lower = input("Enter the lower bound: ")

        if intCheck(lower):
            return int(lower)
        else:
            print("Invalid input. Please enter an integer.")

def upperBound(lower):

    while 1:
        upper = input("Enter the upper bound: ")

        if intCheck(upper):
            upper = int(upper)
            if upper >= lower:
                return int(upper)
            else:
                print("Upper bound must be higher or equal to the lower bound.")
        else:
            print("Invalid input. Please enter an integer.")

def filteredList(numbers, upper, lower):
    return [num for num in numbers if lower <= num <= upper]

def main():
    userNumber = input("Enter an integer (or type 'done' to finish): ")
    numbers = []

    while userNumber != "done":
        if intCheck(userNumber):
            numbers.append(int(userNumber))        
        else:
            print("Input must be an integer. Please try again.")
        userNumber = input("Enter an integer (or type 'done' to finish): ")

    lower = lowerBound()
    upper = upperBound(lower)

    filteredNumbers = str(filteredList(numbers, upper, lower)).replace(",","").replace("[", "").replace("]","")

    print(filteredNumbers)

main()
