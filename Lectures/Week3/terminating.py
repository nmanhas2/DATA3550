from sys import exit
userResponse = input('Enter user response: ')

if not(userResponse == "n" or userResponse == "y"):
    exit("Error: you must enter either n or y")