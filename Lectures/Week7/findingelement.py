values = [17, 25, 5, 30, 100, 96, 48, 5, 14, 30]
x = values.index(96)
print(x)

if 5 in values:
    x = values.index(5)
else:
    x = -1

print(x)

try:
    print(values.index(33))
except ValueError as e:
    print(f"Error: {e}")

#will return True/False
found = 14 in values
print(found)

x = values.index(30)
print(x)
x = values.index(30, x + 1) #second element in index is starting position, third is end position
print(x)
