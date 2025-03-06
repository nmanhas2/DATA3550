try:
    with open("non_existing_file", "r") as file:
        print(file.read9)
except FileNotFoundError as e:
    print(e)