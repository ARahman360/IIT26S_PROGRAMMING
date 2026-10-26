########################################################
# Task A10_T4
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import sys


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    left_index = 0
    right_index = 0
    PMerge.clear()
    while left_index < len(PLeft) and right_index < len(PRight):
        left = PLeft[left_index]
        right = PRight[right_index]
        if (PAsc and left <= right) or (not PAsc and left >= right):
            PMerge.append(left)
            left_index += 1
        else:
            PMerge.append(right)
            right_index += 1
    while left_index < len(PLeft):
        PMerge.append(PLeft[left_index])
        left_index += 1
    while right_index < len(PRight):
        PMerge.append(PRight[right_index])
        right_index += 1
    return None


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return None
    middle = len(PValues) // 2
    left = PValues[:middle]
    right = PValues[middle:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merged: list[int] = []
    merge(left, right, merged, PAsc)
    PValues[:] = merged
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
    mergeSort(values)
    print("Ascending '{}' -> {}".format(filename, ", ".join(str(value) for value in values)))
    mergeSort(values, False)
    print("Descending '{}' -> {}".format(filename, ", ".join(str(value) for value in values)))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
