def main():
    userNumber = int(input("Enter a number: "))

    print(factorial(userNumber))

def factorial(n):
    total = 1

    if n > 0 or n < 0:
        for x in range(1, n + 1):
            total *= x

    return total
main()
