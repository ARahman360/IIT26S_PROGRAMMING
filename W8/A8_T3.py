def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None


def readValues(PFilename: str, PValues: list[float]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                PValues.append(float(line.strip()))
    return None


def calculateSum(PValues: list[float]) -> float:
    return sum(PValues)


def calculateAverage(PValues: list[float]) -> float:
    if len(PValues) == 0:
        return 0.0
    return sum(PValues) / len(PValues)


def main() -> None:
    values: list[float] = []
    print("Program starting.")

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "1":
            filename = input("Insert filename: ")
            readValues(filename, values)
        elif choice == "2":
            print("Amount of values {}".format(len(values)))
        elif choice == "3":
            print("Sum of values {:.1f}".format(calculateSum(values)))
        elif choice == "4":
            print("Average of values {:.1f}".format(calculateAverage(values)))
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
