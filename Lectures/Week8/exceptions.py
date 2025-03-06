try:
    fileName = input("Enter the filename: ")
    with open(fileName, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist")
