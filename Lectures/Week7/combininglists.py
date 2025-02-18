#summing, can also just use sum() once
#you have all the inputs
total = 0.0 
inputStr = input("Enter value: ")
while inputStr != "":
    value = float(inputStr)
    total = total + value
    inputStr = input("Enter value: ")
print(total)

#concatenating, can't use sum()
students = ["Harry", "Cindy", "Emily"]
result = ""
for name in students :
   result = result + name.upper()
print(result)