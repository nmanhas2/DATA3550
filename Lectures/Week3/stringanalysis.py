name = "John Wayne"
print("Way" in name)

name = input('What is your name? ')
if '-' not in name:
    print("The name does not contain a hyphen")
else:
    print("The name does contain a hyphen")

filename = input("Filename: ")
if filename.endswith('.html'):
    print("This is an HTML file")
else:
    print("This is not an HTML file.")

line = input("Line: ")

if line.islower():
    print("The string contains only lowercase letters")
else :
    print("The string contains uppercase letters")

line = input("Line: ")
if line.isalpha():
    print("The string is valid.")
else:
    print("The string must contain only upper or lowercase letters")
    