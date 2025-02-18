def readDate():
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    print(month, day, year)   # Returns a tuple

def main():
    readDate()

main()