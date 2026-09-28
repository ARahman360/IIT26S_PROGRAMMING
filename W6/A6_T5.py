SEPARATOR = ";"


def readValues(filename):
    file = open(filename, "r")
    values = ""

    for row in file:
        number = row.strip()
        if values == "":
            values = number
        else:
            values = values + SEPARATOR + number

    file.close()
    return values


def analyseNumbers(values):
    numbers = values.split(SEPARATOR)

    count = 0
    total = 0
    greatest = 0

    for number in numbers:
        value = int(number)
        count = count + 1
        total = total + value

        if value > greatest:
            greatest = value

    average = total / count
    results = str(count) + SEPARATOR
    results = results + str(total) + SEPARATOR
    results = results + str(greatest) + SEPARATOR
    results = results + "{:.2f}".format(average)
    return results


def showResults(filename, results):
    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print()
    print("#### Number analysis - END ####")
    return None


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseNumbers(values)
    showResults(filename, results)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
