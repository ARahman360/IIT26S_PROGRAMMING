from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    with open(PFilename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip()
            if row != "":
                timestamp = datetime.strptime(row, "%Y-%m-%d %H:%M")
                PTimestamps.append(timestamp)
    return None


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if timestamp.year == PYear:
            count += 1
    return count


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if MONTHS[timestamp.month - 1] == PMonth:
            count += 1
    return count


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for timestamp in PTimestamps:
        if WEEKDAYS[timestamp.weekday()] == PWeekday:
            count += 1
    return count
