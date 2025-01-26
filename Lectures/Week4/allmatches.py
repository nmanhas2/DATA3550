#Suppose you are asked to print the 
#position of each uppercase letter in a
#sentence. You cannot use the for statements
#that iterates over all chars because you need
#to know the positions of the mathces. Instead
#iterate over the postiion (using for with 
# range) and loop up the character at each
#position

string = input("Please enter a string: ")

for index in range(len(string)):
    if string[index].isupper():
        print(index)
