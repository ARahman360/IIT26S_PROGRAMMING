def main():
    word = ""
    print("Program starting.")

    choice = ""
    while choice != "0":
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            word = input("Insert word: ")
        elif choice == "2":
            print('Current word - "' + word + '"')
        elif choice == "3":
            print('Word reversed - "' + word[::-1] + '"')
        elif choice == "0":
            print("Exiting program.")
        else:
            print("Unknown option!")

        print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
