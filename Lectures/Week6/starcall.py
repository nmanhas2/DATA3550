def print_info(name, position, email):
    print("name:", name)
    print("position:", position)
    print("email:", email)

details = ("data analyst", "jake@gmail.com")
print_info("Jake", *details)