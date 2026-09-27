DELIMITER = ","


def collectWords() -> str:
    words = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if words != "":
            words += DELIMITER
        words += word
    return words


def analyseWords(PWords: str) -> None:
    if PWords == "":
        word_count = 0
        character_count = 0
        avg = 0.0
    else:
        words = PWords.split(DELIMITER)
        word_count = len(words)
        character_count = sum(len(word) for word in words)
        avg = character_count / word_count

    print(f"- {word_count} Words")
    print(f"- {character_count} Characters")
    print("- {:.2f} Average word length".format(avg))
    return None


def main() -> None:
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
