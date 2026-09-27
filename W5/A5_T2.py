def frameWord(PWord: str) -> None:
    frame = "*" * (len(PWord) + 4)
    print(frame)
    print("* " + PWord + " *")
    print(frame)
    return None


def main() -> None:
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
