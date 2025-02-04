#Write a program that reads a sequence of grades obtained 
#from the user. It computes the number of passing, and
#failing grades.

#student needs >= 50% to pass

grade = 0
numPassing = 0
numFailing = 0

while grade != -1:
    grade = float(input("Enter a grade or -1 to finish: "))
    if grade < 0 or grade > 100:
        print("Please enter a grade between 0 and 100.")
        break
    elif grade >= 50:
        numPassing += 1
    else:
        numFailing += 1

if grade == -1:
    print(f"Number of passing grades: {numPassing}")
    print(f"Number of failing grades: {numFailing}")

