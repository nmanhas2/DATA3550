total = 0.0
count = 0

inputStr = input("Enter value or 0 to stop: ")

while inputStr != "0":
    value = float(inputStr)
    total = total + value
    count += 1
    inputStr = input("Enter value: ")

if count > 0:
    average = total/count
else:
    average = 0

print(total, average)