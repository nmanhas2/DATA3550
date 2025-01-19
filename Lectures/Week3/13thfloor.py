#  In many countries, the number 13 is considered
#  unlucky. Rather than offending superstitious
#  tenants, building owners sometimes skip the
#  thirteenth floor; floor 12 is immediately 
#  followed by floor 14.

floor = int(input("Which floor number did you press in the elevator? "))

if floor > 13:
    actualFloor = floor -1
else:
    actualFloor = floor

#these are the same outputs
print("Actual Floor %d" % actualFloor)

print("Actual floor", floor-1 if floor > 13 else floor)