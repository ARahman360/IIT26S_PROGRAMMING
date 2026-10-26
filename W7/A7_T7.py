ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def readConfig(PFilename: str) -> tuple[list[str], str]:
    rotors: list[str] = []
    reflector = ""
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Rotor"):
                rotors.append(line.split(":")[1])
            elif line.startswith("Reflector"):
                reflector = line.split(":")[1]
    return rotors, reflector

def rotate(positions: list[int]) -> None:
    positions[0] += 1
    if positions[0] == 26:
        positions[0] = 0
        positions[1] += 1
    if positions[1] == 26:
        positions[1] = 0
        positions[2] += 1
    if positions[2] == 26:
        positions[2] = 0
    return None

def convertCharacter(PLetter: str, PRotors: list[str],
                     PReflector: str, PPositions: list[int]) -> str:
    rotate(PPositions)
    number = ALPHABET.index(PLetter)
    for index in range(3):
        offset = (number + PPositions[index]) % 26
        number = (PRotors[index].index(ALPHABET[offset]) - PPositions[index]) % 26
    number = ALPHABET.index(PReflector[number])
    for index in range(2, -1, -1):
        offset = (number + PPositions[index]) % 26
        number = (ALPHABET.index(PRotors[index][offset]) - PPositions[index]) % 26
    return ALPHABET[number]

def main() -> None:
    filename = input("Insert config(filename): ")
    rotors, reflector = readConfig(filename)
    plugs = input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    print("Enigma initialized.")
    print()
    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            break
        positions: list[int] = [0, 0, 0]
        converted = ""
        for letter in row.upper():
            if letter in ALPHABET:
                new_letter = convertCharacter(letter, rotors, reflector, positions)
                print('Character "{}" illuminated as "{}"'.format(letter, new_letter))
                converted += new_letter
            else:
                converted += letter
        print('Converted row - "{}".'.format(converted))
        print()
    print()
    print("Enigma closing.")
    return None

if __name__ == "__main__":
    main()
