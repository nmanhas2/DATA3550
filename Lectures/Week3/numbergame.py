num = int(input("Please insert a number: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("%d can be divided by 3 and 5" % num)
else:
    print("%d can't be divided by 3 and 5" % num)