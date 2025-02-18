import random

DIE_SIDES = 12

flag = "quit"
userInput = input("Enter the die toss value (or type 'quit' to exit): ")
diceValues = list(range(1, DIE_SIDES + 1))
diceCounts = [0] * DIE_SIDES

while userInput != flag:
    if userInput.isdigit():
        userInput = int(userInput)
        if userInput in diceValues:
            diceCounts[userInput - 1] += 1
    userInput = input("Enter the die toss value (or type 'quit' to exit): ")

for i in range(0, DIE_SIDES):
    print(f"{diceValues[i]}: {diceCounts[i]}")




        
