import time


def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None


def main() -> None:
    duration = 0.0
    print("Program starting.")

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "1":
            duration = float(input("Insert pause duration (s): "))
        elif choice == "2":
            print("Pausing for {} seconds.".format(duration))
            time.sleep(duration)
            print("Unpaused.")
        elif choice == "0":
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
