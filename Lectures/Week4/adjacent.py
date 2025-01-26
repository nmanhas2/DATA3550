strInput = input("Enter an integer value: ")
value = 0
while strInput != "":
    
    previous = value
    value = int(strInput) 

    if value == previous:
        print("Duplicate found")
    
    strInput = input("Enter an integer value: ")
