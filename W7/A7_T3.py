WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            row = line.rstrip("\r\n")
            if row != "":
                PRows.append(row)
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    counts: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for row in PRows:
        for index in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[index] + ";"):
                counts[index] += 1
    for index in range(len(WEEKDAYS)):
        PResults.append(" - {} {} stamps".format(WEEKDAYS[index], counts[index]))
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in PResults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    rows: list[str] = []
    results: list[str] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
