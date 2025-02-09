def main():
    chickens = int(input("Enter the number of chickens: "))
    cows = int(input("Enter the number of cows: "))
    pigs = int(input("Enter the number of pigs: "))

    print(legs(chickens, cows, pigs))

def legs(chickens, cows, pigs):
    chickens = chickens * 2
    cows = cows * 4
    pigs = pigs * 4

    return (chickens + cows + pigs)

main()
