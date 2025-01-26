counter = 0

strInput = input("Enter a number: ")

while strInput != "":
    if(int(strInput) < 0):
        counter += 1
    strInput = input("Enter a number: ")

print(f"There are {counter} negative values.")