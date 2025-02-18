#Write a program that takes a date as input and
#outputs the date's season. The input is a 
#string to represent the month and an int to 
#represent the day. In addition, check if the 
#string and int are valid (an actual month 
#and day).
#
#The dates for each season are:
#Spring: March 20 - June 20
#Summer: June 21 - September 21
#Autumn: September 22 - December 20
#Winter: December 21 - March 19
#
#Make a list containing valid months and days
#while month and day aren't valid:
#Ask user for month
#Ask user for day
#
#Call a function to check the season and output
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def get_month(month):

    while month not in months:
        month = input("Enter the month: ")

    return month

def get_day(month, day):
    days = [31, 28, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]

    monthIndex = months.index(month)

    maxDay = days[monthIndex]

    while not day.isdigit() or int(day) > maxDay or int(day) <= 0:
        
        day = input("Enter the day: ")
    
    return int(day)

def get_season(month, day):
    if (month == 'March' and day >= 20) or (month == 'April' or month == 'May' or month == 'June' and day <= 20):
        return 'Spring'
    elif (month == 'June' and day >= 21) or (month == 'July' or month == 'August' or month == 'September' and day <= 21):
        return 'Summer'
    elif (month == 'September' and day >= 22) or (month == 'October' or month == 'November' or month == 'December' and day <= 20):
        return 'Autumn'
    else:
        return 'Winter'

def main():

    month = ""
    day = ""

    month = get_month(month)
    day = get_day(month, day)
    
    print(f"{month} {day} is the {get_season(month, day)} season.")

main()