#A pedometer treats walking 2,000 steps as walking 1 mile. Write a program whose input is
#the number of steps and whose output is the miles walked. Your program must define and
#call the following function. The function should return the number of miles walked.
#
#steps/2000 = number of miles
#make a function that returns the number of miles, parameter should be number of steps
#ask user for input

def steps_to_miles(steps):
    miles = round(steps/2000, 2)
    
    return miles

def main():
    while 1:
        steps = input("Enter the number of steps: ")

        try:
            steps = int(steps)
            miles = steps_to_miles(steps)
            print(f"{miles} miles walked after walking {steps} steps.")
            break
        except ValueError as error:
            print(f"Error: {error}")
        

main()
        