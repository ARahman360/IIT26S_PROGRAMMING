########################################################
# Task A9_T6
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")
    return None


def saveLines(PLines: list[str]) -> None:
    filename = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as file:
        for line in PLines:
            file.write(line + "\n")
    return None


def main() -> None:
    lines: list[str] = []
    print("Program starting.")

    try:
        while True:
            showOptions()
            choice = input("Your choice: ")

            if choice == "1":
                text = input("Insert text: ")
                lines.append(text)
            elif choice == "2":
                if len(lines) == 0:
                    print("No lines to save.")
                else:
                    saveLines(lines)
                    print("Lines saved.")
            elif choice == "0":
                print("Exiting program.")
                break
            else:
                print("Unknown option!")
            print()

    except KeyboardInterrupt:
        if len(lines) > 0:
            print("Keyboard interrupt and unsaved progress!")
            answer = input("Save before quit(y/n)?: ")
            if answer.lower() == "y":
                saveLines(lines)
        else:
            print("Keyboard interrupt! Program closing suddenly.")

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
