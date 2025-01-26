#In the United States, telephone numbers 
# consist of three parts—area code, 
# exchange, and line number—which are c
# ommonly specified in the form 
# (###)###-####.

#We can examine a string to ensure that it
#contains a correctly formatted phone 
# number with 13 characters.

#To do this, we must not only verify that 
# it contains digits and the appropriate 
# symbols, but that each are in the 
# appropriate spots in the string. 
# This requires an event-controlled loop 
# that can exit early if an invalid 
# character or an out of place symbol 
# is encountered while processing the 
# string:

string = input("Please enter your telephone number in the format of (780)123-4567: ")
valid = len(string) == 13
position = 0
while valid and position < len(string):
    if position == 0:
        valid = string[position] == "("
    elif position == 4 :
        valid = string[position] == ")"
    elif position == 8 :
        valid = string[position] == "-"
    else :
        valid = string[position].isdigit()
    position = position + 1

if valid: 
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")