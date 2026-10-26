########################################################
# Task A10_T7
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import random
random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int) -> None:
    rows = len(PMineField)
    columns = len(PMineField[0]) if rows > 0 else 0
    if PMines < 0 or PMines > rows * columns:
        raise ValueError("Invalid number of mines.")

    placed = 0
    while placed < PMines:
        row = random.randint(0, rows - 1)
        column = random.randint(0, columns - 1)
        if PMineField[row][column] != 9:
            PMineField[row][column] = 9
            placed += 1
    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    for row in range(rows):
        for column in range(len(PMineField[row])):
            if PMineField[row][column] == 9:
                continue
            count = 0
            for row_offset in (-1, 0, 1):
                for column_offset in (-1, 0, 1):
                    next_row = row + row_offset
                    next_column = column + column_offset
                    if 0 <= next_row < rows:
                        if 0 <= next_column < len(PMineField[next_row]):
                            if PMineField[next_row][next_column] == 9:
                                count += 1
            PMineField[row][column] = count
    return None


def generateMinefield(PMineField: list[list[int]], PRows: int,
                      PCols: int, PMines: int) -> None:
    if PRows <= 0 or PCols <= 0 or PMines < 0 or PMines > PRows * PCols:
        raise ValueError("Invalid board size or mine count.")
    PMineField.clear()
    for row in range(PRows):
        PMineField.append([])
        for column in range(PCols):
            PMineField[row].append(0)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None


def showOptions() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")
    return None


def main() -> None:
    field: list[list[int]] = []
    print("Program starting.")
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            columns = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            try:
                generateMinefield(field, rows, columns, mines)
            except ValueError as error:
                print(error)
        elif choice == "2":
            for row in field:
                print(row)
        elif choice == "3":
            if len(field) == 0:
                print("Generate a board first.")
            else:
                filename = input("Insert filename: ")
                with open(filename, "w", encoding="utf-8") as file:
                    for row in field:
                        file.write(",".join(str(value) for value in row) + "\n")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    field.clear()
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
