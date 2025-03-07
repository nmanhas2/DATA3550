fileName = "chp7_b_pre_1.txt"
toWrite = []

with open(fileName, "w") as file:
    file.writelines(["John Smith: 89\n",
           "Mary Davis: 92\n",
           "Adam Li: 85\n",
           "Mohamed Ali: 78"])

file.close()

try:
    with open(fileName, "r") as file:
        print(file.readlines())
except FileNotFoundError as e:
    print(e)
