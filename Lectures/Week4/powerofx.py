#Constant variables for max ranges
#n = exponent 
#x = base
NMAX = 4
XMAX = 10

#print table header
for n in range (1, NMAX + 1):
    print("%10d" % n, end="")

print()
for n in range(1, NMAX + 1):
    print("%10s" % "x ", end="")

print("\n", "    ", "-" * 35)

#Print table body
for x in range(1, XMAX + 1):
    #Print the x row in the table
    for n in range (1, NMAX + 1):
        print("%10.0f" % x ** n, end="")
    
    print()