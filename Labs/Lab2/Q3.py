#write an if-else statement with multiple
#branches. If year is 2101 or later, print
#Distant future. Otherwise, if the year is
#2001 or greater, print 21st century. Otherwise,
#if the year is 1901 or greater, print 20th century
#Else, 1900 or earlier, print Long ago

#if year >= 2101 print Distant future
#elif year >= 2001 print 21st century
#elif year >= 1901, print 20th century
#else print long ago

year = input("Enter the year: ")

if year.isdigit() and int(year) > 0:  
    if year >= 2101:
        print("Distant future")
    elif year >= 2001:
        print("21st century")
    elif year >= 1901:
        print("20th century")
    else:
        print("Long ago")
else:
    print("Please enter a positive integer.")
    