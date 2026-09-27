def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice():
    answer = input("Your choice: ")
    if answer.isnumeric():
        choice = int(answer)
    else:
        choice = -1
    return choice


def main():
    count = 0
    choice = -1
    print("Program starting.")

    while choice != 0:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print("Current count -", count)
        elif choice == 2:
            count = count + 1
        elif choice == 3:
            count = 0
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")

        print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
