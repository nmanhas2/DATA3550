#4. Write a program to compute how many gallons of paint are needed to cover the walls
#given square feet. 1 gallon = 350 sqr ft. Gallons = sqr ft / 350.0
#Ex: If input = 250.0, the output should be 0.714284714286
GALLONS_CONVERSION_FACTOR = 350.0

userInput = input("Enter the area of wall to cover in paint (in square feet): ")

wallArea = int(userInput)

print("We need %.2f gallon(s) of paint." % (wallArea/GALLONS_CONVERSION_FACTOR))
