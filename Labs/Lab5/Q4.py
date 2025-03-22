def main():
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")

    string1 = set(string1)
    string2 = set(string2)

    inBoth = sorted(string1.intersection(string2))
    
    exclusive = sorted(string1.difference(string2))

    print("The characters that are in both strings:")

    for word in inBoth:
        print(word, end="")

    print("\nThe characters in string 1 that are not in string 2: ")

    for ex in exclusive:
        print(ex, end="")

if __name__ == "__main__":
    main()