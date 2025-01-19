#write a python program that asks the user to enter three integrer numbers. The program shouldd output the largest of
#the three numbers
# if num1 > num2 if num1 > num3
# if num2 > num1 if num2 > num3
# else

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

#could also just do this
print(max(num1, num2, num3))
