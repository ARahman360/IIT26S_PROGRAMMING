########################################################
# Task A10_T3
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import sys


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    length = len(PValues)
    for iteration in range(length - 1):
        for index in range(length - iteration - 1):
            first = PValues[index]
            second = PValues[index + 1]
            if (PAsc and first > second) or (not PAsc and first < second):
                PValues[index] = second
                PValues[index + 1] = first
    return None


def readValues(PFilename: str) -> list[int]:
    values: list[int] = []
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                values.append(int(line.strip()))
    return values


def main() -> None:
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values = readValues(filename)
    print("Raw '{}' -> {}".format(filename, ", ".join(str(value) for value in values)))
    bubbleSort(values)
    print("Ascending '{}' -> {}".format(filename, ", ".join(str(value) for value in values)))
    bubbleSort(values, False)
    print("Descending '{}' -> {}".format(filename, ", ".join(str(value) for value in values)))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
