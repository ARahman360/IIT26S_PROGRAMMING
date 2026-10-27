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
        return int(answer)
    return -1


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
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")

        print()

    print("Program ending.")
    return None


# The assignment's tests import/reload the file named main.py to run it.
# Importing this original A5_T6.py by name will not start an input loop.
if __name__ in ("__main__", "main"):
    main()
