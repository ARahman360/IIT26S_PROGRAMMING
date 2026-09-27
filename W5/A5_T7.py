DELIMITER = ","


def collectWords():
    allWords = ""
    word = input("Insert word(empty stops): ")

    while word != "":
        if allWords == "":
            allWords = word
        else:
            allWords = allWords + DELIMITER + word
        word = input("Insert word(empty stops): ")

    return allWords


def analyseWords(PWords):
    wordCount = 0
    characterCount = 0
    avg = 0

    if PWords != "":
        words = PWords.split(DELIMITER)
        wordCount = len(words)

        for word in words:
            characterCount = characterCount + len(word)

        avg = characterCount / wordCount

    print("-", wordCount, "Words")
    print("-", characterCount, "Characters")
    print("- {:.2f} Average word length".format(avg))
    return None


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
