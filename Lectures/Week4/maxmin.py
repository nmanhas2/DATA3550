largest = float(input("Enter a value: "))
strInput = input("Enter a value: ")

while strInput != "":
    value = float(strInput)
    if value > largest:
        largest = value
    strInput = input("Enter a value: ")

print(f"Largest value is {value}")

