import matplotlib.pyplot as plt
import numpy as np

def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)

quadratic_algo([4, 5, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [4, 16, 36, 64, 100, 144]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Quadratic Complexity')
plt.show()