import matplotlib.pyplot as plt
import time

def linear(n):
    return n ** 2

def quadratic_bigo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' ,item2)

quadratic_bigo([4, 5, 6, 8])

steps = []

for i in range(1, 100):
    steps.append(linear(i))

plt.plot(steps)
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.show()