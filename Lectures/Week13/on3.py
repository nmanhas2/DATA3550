import matplotlib.pyplot as plt

def linear(n):
    return n ** 3

def cubic_big_o(list1):
    for item1 in list1:
        for item2 in list1:
            for item3 in list1:
                print(item1, item2, item3)

cubic_big_o([1,2,3])

steps = []

for i in range(1, 100):
    steps.append(linear(i))

plt.plot(steps)
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.show()