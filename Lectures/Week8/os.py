import os
name = os.getcwd()
print(name)

filename = "scores.txt"

if os.path.exists(filename):
    inputFile = open(filename)
else:
    print(f"{filename} doesn't exist")

contents = os.listdir()

for fname in contents:
    print(fname) 

if os.path.isdir(filename):
    print(filename, "is a directory")
else:
    print("Not a directory")