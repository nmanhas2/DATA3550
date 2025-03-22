def getAcronym(phrase):
    myWords = phrase.split()

    acronym = (word[0] for word in myWords if word[0].isupper())
    acronym = "".join(acronym)
    return acronym

def getInput(prompt):
    while 1:
        myInput = input(prompt)
        noSpaces = myInput.replace(" ", "")
        if noSpaces.isalpha() and noSpaces.isalnum():       
            return myInput
        else:
            print("Invalid phrase. ")

def main():
    sentence = getInput("Enter a phrase: ")
    acronym = getAcronym(sentence)

    print(acronym)

if __name__ == "__main__":
    main()