#Algorithm for finding the first letter x
#in a string

string = input("Enter a string: ")
found = False
ch ="?"
pos = 0

while not found and pos < len(string) :
    ch = string[pos]
    if ch =="x":
        found = True
    else:
        pos = pos + 1

if found:
    print("Found letter 'x' at index", pos)
else:
    print("Not found")