########################################################
# Task A10_T2
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip()
            if row != "":
                PValues.append(int(row))
    return None


def sumOfValues(PValues: list[int]) -> int:
    total = 0
    for value in PValues:
        total += value
    return total


def productOfValues(PValues: list[int]) -> int:
    product = 1
    for value in PValues:
        product *= value
    return product


def main() -> None:
    values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, values)
    print("# --- Sum of numbers --- #")
    print(sumOfValues(values))
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(productOfValues(values))
    print("# --- Product of numbers --- #")
    values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
