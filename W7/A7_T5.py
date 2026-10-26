from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

@dataclass
class DAY_USAGE:
    weekday: str = ""
    consumption: float = 0.0
    cost: float = 0.0

def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            row = line.rstrip("\r\n")
            if row != "":
                columns = row.split(DELIMITER)
                timestamp = TIMESTAMP()
                timestamp.weekday = "Saturday" if columns[0] == "Saturnday" else columns[0]
                timestamp.hour = columns[1]
                timestamp.consumption = float(columns[2])
                timestamp.price = float(columns[3])
                PTimestamps.append(timestamp)
    return None

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    daily: list[DAY_USAGE] = []
    PResults.clear()
    for weekday in WEEKDAYS:
        day = DAY_USAGE()
        day.weekday = weekday
        daily.append(day)
    for timestamp in PTimestamps:
        for day in daily:
            if timestamp.weekday == day.weekday:
                day.consumption += timestamp.consumption
                day.cost += timestamp.consumption * timestamp.price
    for day in daily:
        result = " - {} usage {:.2f} kWh, cost {:.2f} €".format(
            day.weekday, day.consumption, day.cost)
        PResults.append(result)
    daily.clear()
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for result in PResults:
        print(result)
    print("### Electricity consumption summary ###")
    return None

def main() -> None:
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)
    timestamps.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
