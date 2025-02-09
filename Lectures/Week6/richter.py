def main():
    userInput = float(input("Richter scale: "))
    richter(userInput)

def richter(richterNumber):
    if richterNumber >= 8.0:
        print("Most structures fall")
    elif richterNumber >= 7.0 :
        print("Many buildings destroyed")
    elif richterNumber >= 6.0 :
        print("Many buildings considerably damaged, some collapse")
    elif richterNumber >= 4.5 :
        print("Damage to poorly constructed buildings")
    else :
        print("No destruction of buildings")

main()