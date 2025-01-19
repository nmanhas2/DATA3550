#Your task is to extract a string containing  the middle character from a given string
#Even numbers shoul extract the middle two chars
#if length of string is odd, grab the middle char
#if length of string is even, grab the middle two
#if len(string) % 2 == 0
#   string[int((len/2))] + string[int(len/2))]

userString = input("Enter a string: ")

length = len(userString)
middle = (length // 2) - 1
print(3//2)
if length % 2 == 0:
    print(userString[middle] + userString[middle + 1])
else:
    print(userString[middle + 1])


