def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")

    print('Reading names from "' + filename + '".')
    file = open(filename, "r")

    names = ""
    for row in file:
        name = row.strip()
        if name != "":
            if names == "":
                names = name
            else:
                names = names + ";" + name
    file.close()

    print("Analysing names...")
    nameList = names.split(";")

    count = len(nameList)
    shortest = len(nameList[0])
    longest = len(nameList[0])
    total = 0

    for name in nameList:
        length = len(name)
        total = total + length

        if length < shortest:
            shortest = length
        if length > longest:
            longest = length

    average = total / count
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count -", count)
    print("Shortest name -", shortest, "chars")
    print("Longest name -", longest, "chars")
    print("Average name - {:.2f} chars".format(average))
    print("#### REPORT END ####")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
