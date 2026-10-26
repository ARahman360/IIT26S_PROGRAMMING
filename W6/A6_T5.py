SEPARATOR = ";"


def readValues(filename):
    with open(filename, "r") as file:
        return SEPARATOR.join(row.strip() for row in file)


def analyseValues(values):
    numbers = [int(number) for number in values.split(SEPARATOR)]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    return "Count;Sum;Greatest;Average\n{};{};{};{:.2f}\n".format(
        count, total, greatest, average
    )


def analyseNumbers(values):
    return analyseValues(values).splitlines()[1]


def showResults(filename, results):
    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    print(results, end="")
    print()
    print("#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseValues(values)
    showResults(filename, results)
    print("Program ending.")


if __name__ == "__main__":
    main()
