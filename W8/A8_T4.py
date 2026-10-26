from datetime import datetime
import A8_T4_Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None


def main() -> None:
    timestamps: list[datetime] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    A8_T4_Lib.readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "1":
            year = int(input("Insert year: "))
            count = A8_T4_Lib.calculateYears(year, timestamps)
            print("Amount of timestamps during year '{}' is {}".format(year, count))
        elif choice == "2":
            month = input("Insert month: ")
            count = A8_T4_Lib.calculateMonths(month, timestamps)
            print("Amount of timestamps during month '{}' is {}".format(month, count))
        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = A8_T4_Lib.calculateWeekdays(weekday, timestamps)
            print("Amount of timestamps during weekday '{}' is {}".format(weekday, count))
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    timestamps.clear()
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
