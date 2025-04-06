import matplotlib.pyplot as plt
import numpy as np

def linear_algo(items):
    #O(n) for just one loop, O(2n) for two loops, but in 
    #a scenario of infinite inputs the "2" isn't relevant
    #since 2 * infinity is still infinity
    for item in items:
        print(item)
    
    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [4, 8, 12, 16, 20, 24]

#y = 2n, but the output is still linear as it would be with one loop
plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()