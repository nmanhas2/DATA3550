MAX_COUNT = 10
count = 0
myList = []

while count < 10:
    userInput = input("Enter a number: ")
    try:
        userInput = float(userInput)
        if userInput not in myList:
        
            myList.append(userInput)
            count+=1
    except ValueError as e:
        print(f"Error: {e}")
    
myList = str(myList)
print(myList[1:len(myList)-1]) #removing the '[' and ']'