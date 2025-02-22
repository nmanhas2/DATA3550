infile = open("ex1.txt", "r")
outfile = open("ex4.txt", "w")

total = 0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write("%8.2f\n" % value)
    total = total + value
    count += 1
    line = infile.readline()

average = total / count

outfile.write("Total : %6.2f \n" % total)
outfile.write("Average : %6.2f \n" % average)



