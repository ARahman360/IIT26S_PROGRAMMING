LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(character, alphabets, shift=13):
    if character not in alphabets:
        return character
    return alphabets[(alphabets.index(character) + shift) % len(alphabets)]


def rot13(content):
    result = ""
    for character in content:
        if character in LOWER_ALPHABETS:
            result += shiftCharacter(character, LOWER_ALPHABETS)
        elif character in UPPER_ALPHABETS:
            result += shiftCharacter(character, UPPER_ALPHABETS)
        else:
            result += character
    return result


def cipherText(text):
    return rot13(text)


def askRows():
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    return "\n".join(rows) + ("\n" if rows else "")


def writeFile(filename, content):
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(content)


def main():
    print("Program starting.")
    print()
    plain_text = askRows()
    ciphered_text = rot13(plain_text)
    print()
    print("#### Ciphered text ####")
    print(ciphered_text, end="\n")
    print("#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename:
        writeFile(filename, ciphered_text)
        print("Ciphered text saved!")
    else:
        print("File name not defined.")
        print("Aborting save operation.")
    print("Program ending.")


if __name__ == "__main__":
    main()
