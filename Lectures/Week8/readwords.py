def read_words(fileName):
    with open(fileName, "r") as file:
        words = file.read().split()
        print(words)
        return words

def main():
    fileName = input("Enter the fileName: ")
    words = read_words(fileName)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()