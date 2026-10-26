from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

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
                timestamp.weekday = columns[0]
                timestamp.hour = columns[1]
                timestamp.consumption = float(columns[2])
                timestamp.price = float(columns[3])
                PTimestamps.append(timestamp)
    return None

def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    readFile(filename, timestamps)


def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for timestamp in timestamps:
        total = timestamp.consumption * timestamp.price
        print(" - {} {}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            timestamp.weekday, timestamp.hour, timestamp.price,
            timestamp.consumption, total))
    return None


def main() -> None:
    timestamps: list[TIMESTAMP] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    timestamps.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
