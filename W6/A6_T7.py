LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PLACES = ["home", "Galba's palace", "Otho's palace", "Vitellius' palace",
          "Vespasian's palace"]


def rot13(text):
    result = ""

    for character in text:
        if character in LOWER_ALPHABETS:
            position = LOWER_ALPHABETS.index(character)
            result = result + LOWER_ALPHABETS[(position + 13) % 26]
        elif character in UPPER_ALPHABETS:
            position = UPPER_ALPHABETS.index(character)
            result = result + UPPER_ALPHABETS[(position + 13) % 26]
        else:
            result = result + character

    return result


def main():
    print("Travel starting.")

    file = open("player_progress.txt", "r")
    rows = file.readlines()
    file.close()

    lastRow = rows[-1].strip().split(";")
    currentLocation = int(lastRow[0])
    nextLocation = int(lastRow[1])
    passphrase = lastRow[2]

    plainPassphrase = rot13(passphrase)

    print("Currently at " + PLACES[currentLocation] + ".")
    print("Travelling to " + PLACES[nextLocation] + "...")
    print("...Arriving to the " + PLACES[nextLocation] + ".")
    print("Passing the guard at the entrance.")
    print('"' + plainPassphrase.capitalize() + '!"')
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    messageFilename = str(nextLocation) + "_" + passphrase + ".gkg"
    file = open(messageFilename, "r")
    messageRows = file.readlines()
    file.close()

    progress = messageRows[0].strip()

    file = open("player_progress.txt", "a")
    file.write(progress + "\n")
    file.close()
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    plainMessage = ""
    for row in messageRows[1:]:
        plainMessage = plainMessage + rot13(row)

    plainFilename = str(nextLocation) + "-" + plainPassphrase + ".txt"
    file = open(plainFilename, "w")
    file.write(plainMessage)
    file.close()

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
    return None


if __name__ == "__main__":
    main()
