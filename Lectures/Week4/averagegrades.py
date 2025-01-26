#It is common to repeatedly read and 
# process multiple groups of values. Write 
# a program that can be used to compute the 
# average exam grade for multiple students. 
# Each student has the same number of exam 
# grades

#Compute the average grade for one student
#Repeat the process for each student

#Ask for how many exams

numberOfExams = int(input("How many exams did you have? "))

moreGrades = "Y"

while moreGrades == "Y":
    print("Enter the exam grades: ")
    total = 0
    for examNum in range(1, numberOfExams + 1):
        currentExamScore = int(input(f"Enter exam {examNum} score: "))
        total = total + currentExamScore
    average = total / numberOfExams

    moreGrades = input("Would you like to enter another student(Y/N)? ")
    moreGrades = moreGrades.upper()