#Every 4 years is  a leap year, every 100 years it get ommitted, every 400 years another leap year is ommitted
# if year is divisble by 4 it's a leap year
# if year is divisble by 100 it's not a leap year
# if year is divisble by 400 it's a leap year

year = input("Enter the year: ")

if year.isdigit():
    year = int(year)
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
        print("%d is a leap year" % year)
    else:
        print("%d is not a leap year" % year)
else:
    print("Invalid input, please enter a number")