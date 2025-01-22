#Write a program that reads a floating-point 
#number and prints "zero" if the number is
#zero. Otherwise, print "positive" or "negative"
#Add small if the absoulte value of the number 
#is less than 1,000,000 or big if it exceeds
#1,000,000

#if number = 0, print 0
#elif number is pos, print positive
#else number is negative, print negative

#if number < 1,000,000 print small
#else print big

THRESHOLD = 1000000

userNumber = float(input("Enter a number: "))

if userNumber == 0:
    myOutput = "zero"
else:
    if abs(userNumber) > THRESHOLD:
        size = "large"
    else:
        size = "small"

    if userNumber > 0:
        sign = "positive"
    else:
        sign = "negative"

print(f"{size} {sign}")