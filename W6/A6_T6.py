LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cipherText(text):
    ciphered = ""

    for character in text:
        if character in LOWER_ALPHABETS:
            position = LOWER_ALPHABETS.index(character)
            newPosition = (position + 13) % 26
            ciphered = ciphered + LOWER_ALPHABETS[newPosition]
        elif character in UPPER_ALPHABETS:
            position = UPPER_ALPHABETS.index(character)
            newPosition = (position + 13) % 26
            ciphered = ciphered + UPPER_ALPHABETS[newPosition]
        else:
            ciphered = ciphered + character

    return ciphered


def main():
    print("Program starting.")
    print()
    print("Collecting plain text rows for ciphering.")

    cipheredText = ""
    row = input("Insert row(empty stops): ")

    while row != "":
        cipheredText = cipheredText + cipherText(row) + "\n"
        row = input("Insert row(empty stops): ")

    print()
    print("#### Ciphered text ####")
    print(cipheredText, end="")

    filename = input("Insert filename to save: ")
    file = open(filename, "w")
    file.write(cipheredText)
    file.close()

    print("Ciphered text saved!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
