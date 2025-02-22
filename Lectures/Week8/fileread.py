infile = open("example1.txt", "r")
line = infile.readline(4) #print out four chars from file
print(line)

line = infile.readline() #reads one line
print(line)

line = infile.readline() #reads one line
print(line)

line = infile.readline() #reads one line
print(line)

infile.close()

#Different ways of reading multiple lines
with open("example1.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())
    file.close()

with open("example1.txt") as file:
    content = file.read()
    print(content)
file.close()