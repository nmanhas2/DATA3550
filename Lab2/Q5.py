#Write a program that reads a temperature
#value and the letter C for celsius or F
#for Fahrenheit. Print whether water is
#liquid, solid, or gaseous given temp at
#sea level

#if input is a digit
#   if other input is F or f
#       if input > 212F print gaseous
#       elif input < 32 print solid
#       else print liquid
#   elif input is C or c
#       if input > 100 print gaseous
#       elif input < 0 print solid
#       else print liquid
#else error

temperature = input("Enter the temperature: ")
unit = input("Enter the unit of temperature (C/F): ")

if temperature.isdigit():
    temperature = int(temperature)
    if unit == "F" or unit == "f":
        if temperature >= 212:
            print("At that temperature, the water is gaseous.")
        elif temperature < 32:
            print("At that temperature, the water is solid.")
        else:
            print("At that temperature, the water is liquid")
    elif unit == "C" or unit == "c":
        if temperature >= 100:
            print("At that temperature, the water is gaseous.")
        elif temperature < 0:
            print("At that temperature, the water is solid.")
        else:
            print("At that temperature, the water is liquid")
    else:
        print("Please enter a valid unit of temperature.")
else:
    print("Please enter an integer.")