from builtins import sum

def get_average(*args):
    total = sum(args)
    return total / len(args)

print(get_average(5, 10, 15))
print()

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(age=24, position="data analyst")