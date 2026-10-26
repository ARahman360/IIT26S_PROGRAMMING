########################################################
# Task A10_T6
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import copy
import time
from typing import Callable


def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                PValues.append(int(line.strip()))
    return None


def bubbleSort(PNums: list[int]) -> list[int]:
    for iteration in range(len(PNums) - 1):
        for index in range(len(PNums) - iteration - 1):
            if PNums[index] > PNums[index + 1]:
                PNums[index], PNums[index + 1] = PNums[index + 1], PNums[index]
    return PNums


def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    smaller = []
    equal = []
    larger = []
    for number in PNums:
        if number < pivot:
            smaller.append(number)
        elif number > pivot:
            larger.append(number)
        else:
            equal.append(number)
    return quickSort(smaller) + equal + quickSort(larger)


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    start_time = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end_time = time.perf_counter_ns()
    return end_time - start_time


def showOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")
    return None


def main() -> None:
    values: list[int] = []
    results: list[str] = []
    filename = ""
    print("Program starting.")
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            filename = input("Insert dataset filename: ")
            readValues(filename, values)
            results.clear()
        elif choice == "2":
            if filename == "":
                print("Read dataset values first.")
            else:
                built_in = measureSortingTime(sorted, copy.deepcopy(values))
                bubble = measureSortingTime(bubbleSort, copy.deepcopy(values))
                quick = measureSortingTime(quickSort, copy.deepcopy(values))
                results.clear()
                results.append("Measured speeds for dataset '{}':".format(filename))
                results.append(" - Built-in sorted {} ns".format(built_in))
                results.append(" - Buble sort {} ns".format(bubble))
                results.append(" - Quick sort {} ns".format(quick))
                for row in results:
                    print(row)
        elif choice == "3":
            if len(results) == 0:
                print("Measure speeds first.")
            else:
                result_filename = input("Insert results filename: ")
                with open(result_filename, "w", encoding="utf-8") as file:
                    for row in results:
                        file.write(row + "\n")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    values.clear()
    results.clear()
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
