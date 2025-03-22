#Q2
#ask for file
#Open file, w/ proper checks
#readlines, w/ strip, return list
#ask for lower bound, ask for upper bound
#filter w/ new list

def getFile():
    prompting = None

    while 1:
        try:
            fileName = input("Enter your file name: ")
            file = open(fileName, 'r')
            words = file.readlines()
            return[word.strip() for word in words]
        except Exception as e:
            print(e)

def filterWords(words, lowerBound, upperBound):
    filteredWords = [word for word in words if lowerBound <= word <= upperBound]
    if len(filteredWords) == 0:
        return ["Beyond the search range."]
    else:
        return filteredWords

def main():
    words = getFile()
    lowerBound = input("Enter the lower bound of the search: ")
    upperBound = input("Enter the upper bound of the search: ")

    filteredWords = filterWords(words, lowerBound, upperBound)

    for word in filteredWords:
        print(word)

if __name__ == '__main__':
    main()
