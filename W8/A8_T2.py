import A8_T2_Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None


def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    return -1


def askValue(PPrompt: str) -> float:
    value = float(input(PPrompt))
    return value


def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            first = askValue("Insert first addend value: ")
            second = askValue("Insert second addend value: ")
            result = A8_T2_Lib.add(first, second)
            print("{} + {} = {}".format(first, second, result))
        elif choice == 2:
            first = askValue("Insert minuend value: ")
            second = askValue("Insert subtrahend value: ")
            result = A8_T2_Lib.subtract(first, second)
            print("{} - {} = {}".format(first, second, result))
        elif choice == 3:
            first = askValue("Insert multiplicant value: ")
            second = askValue("Insert multiplier value: ")
            result = A8_T2_Lib.multiply(first, second)
            print("{} * {} = {}".format(first, second, result))
        elif choice == 4:
            first = askValue("Insert dividend value: ")
            second = askValue("Insert divisor value: ")
            if second == 0:
                print("Cannot divide by zero.")
            else:
                result = A8_T2_Lib.divide(first, second)
                print("{} / {} = {}".format(first, second, result))
        else:
            print("Unknown option!")
        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
