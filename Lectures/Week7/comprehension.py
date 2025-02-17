#The first usage of list comprehension is to perform an operation on all elements of a 
# sequence. 
#As an example consider a list containing the numbers from 1 to 20. In order to create a
#  list containing the squares of these numbers the following Python code can be used.

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8]
square = []

for num in numbers:
  square.append(num * num)

print(square)

#It is even possible to use multiple lists inside a list comprehension. For example, to 
# create a list containing all the combinations of two lists the following list 
# comprehension can be used. This is much more concise and therefore more readable 
# as the standard approach using two nested for loops.

letters = ["A", "B", "C"]
numbers = [1, 2, 3]

combinations = [l + str(n) for l in letters for n in numbers]

print("The possible combinations of letters and numbers are:", combinations)

firstNames = ["Joe", "Jim", "Betsy", "Shelly"]
lastNames = ["Jones", "Patel", "Hicks", "Smith", "Lee"]
fullNames = [f + l for f in firstNames for l in lastNames]
print(fullNames)

#As mentioned in the introduction, list comprehensions are also very useful in order to
#  filter existing sequences. As an example consider a list containing songs and the 
# number of times these songs were played. In order to create a list with all songs that
#  were played at least 30 times, the following Python code could be used.

songs = [
    ["Ace of Spades", 99],
    ["Anarchy in the UK", 51],
    ["Blitzkrieg Bop", 17],
    ["Blue Train", 42],
    ["Dirty", 23],
    ["No Sleep Til Brooklyn", 15],
    ["Paranoid", 33],
]

pop_song = []
for element in songs :
  if element[1] > 42 :
    pop_song.append(element[0])

print(pop_song)