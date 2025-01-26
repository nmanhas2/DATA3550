valid = False

while not valid:
    value = int(input("Enter a postitve integer value < 100: "))
    if value > 0 and value < 100:
        valid = True
    else:
        print("Invalid input")

