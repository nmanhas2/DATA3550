#initialize a list with 26 elements initialized to 0
letterCounts = [0] * 26

#open the file for reading
with open('paragraph.txt', 'r') as file:
    #Iterate through each line in the file
    for line in file:
        #iterate through each character in the line
        for char in line:
            char = char.upper()
            #check if the char is an uppercase letter
            if 'A' <= char <= 'Z':
                #calculate the index for letterCounts list
                code = ord(char) - ord("A")
                #increment the count for the corresponding letter
                letterCounts[code] += 1

for i in range(26):
    letter = chr(ord('A') + i)
    print(f"{letter}: {letterCounts[i]}")


letterCounts = [0] * 26
# The file contains 'Home computers are being called upon to perform many new
# functions, including the consumption of homework formerly eaten by
# the dog. ~Doug Larson'

file = "dongye_output2.txt"
inputFile = open(file, "r")

char = inputFile.read(1)
while char != "" :
   char = char.upper()
   if char >= "A" and char <= "Z" :
      code = ord(char) - ord("A")
      letterCounts[code] = letterCounts[code] + 1
   char = inputFile.read(1)

inputFile.close()
print(letterCounts[1])
