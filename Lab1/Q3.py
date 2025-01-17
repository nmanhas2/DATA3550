#3. Write a program that prompts the user for a measurement in meters and then converts
#it to miles, feet, and inches

#Basing these conversion factors from Test Case No. 2
MILES_CONVERSION_FACTOR = 0.000621371
FEET_CONVERSION_FACTOR = 3.28084
INCHES_CONVERSION_FACTOR = 39.37007857

userMeasurement = input("Enter a measure (in meters):")

meters = float(userMeasurement)
miles = meters * MILES_CONVERSION_FACTOR
feet = meters * FEET_CONVERSION_FACTOR
inches = meters * INCHES_CONVERSION_FACTOR

print(meters, "meters is %.2f miles." % miles)
print(meters, "meters is %.2f feet." % feet)
print(meters, "meters is %.2f inches." % inches)
