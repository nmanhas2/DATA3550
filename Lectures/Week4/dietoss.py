#This program simulates tosses of a pair
#of dice

from random import randint

for i in range(10):
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print(d1, d2)