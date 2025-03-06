path = "C:/Users/manha/OneDrive/Documents/DATA3550/DATA3550/Lectures/Week8/chp7_hr.csv"
try:
    with open(path, "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

try:
    with open("newfile.txt", "w") as file:
        print(file.write("hello"))
except FileNotFoundError as e:
    print(e)