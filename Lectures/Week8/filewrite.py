outF = open("example1.txt", "w")
outF.write("This is an example!\n Hello world! \n Fortnite!")
outF.close()

#printing out text from a file
with open("example1.txt") as f:
    [print(line.strip()) for line in f.readlines()]