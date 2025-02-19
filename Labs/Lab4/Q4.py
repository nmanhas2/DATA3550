done = "done"
numbersList = []
userInput = input("Enter a number to add to the list: ")

while 1:

    if userInput != done or len(numbersList) % 2 != 0:
        
        if userInput.replace('.','').replace('-','').isdigit():
            numbersList.append(float(userInput))

        userInput = input("Enter a number to add to the list: ")
    else:
        break

middle = len(numbersList) // 2

jointList = str(numbersList[middle:] + numbersList[:middle])

print(jointList[1:len(jointList)-1])
