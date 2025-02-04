#My test case: input = -9999.562, output was "small negative"

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
        sign = " positive"
    else:
        sign = " negative"

    myOutput = size + sign

print(f"{myOutput}")