values = []
n = int(input("Enter an integer: "))
for i in range(n) :
   values.append(i * i)
print(values)


#Given the list values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#which statement fills the list with the following numbers?
#1 4 9 16 25 36 49 64 81 100
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(1, len(values) + 1):
   values[x-1] = x*x
print(values)