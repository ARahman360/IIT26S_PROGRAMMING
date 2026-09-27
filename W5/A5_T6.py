def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice() -> int:
    feed = input("Your choice: ")
    if feed.isnumeric():
        return int(feed)
    return -1


def main() -> None:
    count = 0
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
        elif choice == 3:
            count = 0
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
