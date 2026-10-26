########################################################
# Task A10_T1
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def readValues(PFilename: str, PValues: list[str]) -> None:
    PValues.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            value = line.strip()
            if value != "":
                PValues.append(value)
    return None


def main() -> None:
    values: list[str] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, values)

    print("# --- Vertically --- #")
    for value in values:
        print(value)
    print("# --- Vertically --- #")

    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

    values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
