total = 0.00
count = 0
salary = 0.00

while salary >= 0.00:
    salary = input("Please enter your salary amount or -1 to quit: ")
    salary = float(salary)
    if salary >= 0.00 :
        total = total + salary
        count += 1
    
if count > 0:
    average = total / count
    print("Average salary is", average, ".")
else:
    print("No data was entered.")