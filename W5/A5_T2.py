def frameWord(PWord):
    stars = "*" * (len(PWord) + 4)
    print(stars)
    print("* " + PWord + " *")
    print(stars)
    return None


def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
