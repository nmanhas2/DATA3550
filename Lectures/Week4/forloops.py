#These two are he same
for i in range(6, 10):
    print(i)

i = 6
while i < 10:
    print(i)
    i+=1

#end="" will make it all appear on the same 
#line, by deafult it's "\n", which is why
#print starts on a new line
for j in range(5):
    value = j* 2
    print("%d, " %value, end="")

#You can add spaces in between on the same line
print("\n")
name = "Fred"
for ch in name:
    print(ch, end=" ")

#You can change the steps, end with range as well
print("\n")
for i in range(len(name) -1, -1, -1):
    print(name[i], end=" ")

#Remember that it's exclusive, ie. stop is
#ommitted!
print("\n")
for i in range(0, 8, 2):
    print("%d " % i, end = "")

#You can use breaks in for loops too
company = ["W", "R", "T", "F", "H", "E", "K", "A"]
for i in company:
    if i == "H":
        break
    print(i)
