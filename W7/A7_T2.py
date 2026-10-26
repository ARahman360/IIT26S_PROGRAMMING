def main() -> None:
    numbers: list[int] = []
    print("Program starting.")
    values = input("Insert comma separated integers: ")
    for value in values.split(","):
        value = value.strip()
        try:
            number = int(value)
            numbers.append(number)
        except ValueError:
            print('Invalid value "{}".'.format(value))
    if len(numbers) == 0:
        print("No integers to analyze.")
    else:
        total = sum(numbers)
        print("There are {} integers in the list.".format(len(numbers)))
        if total % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        print("Sum of the integers is {} and it's {}".format(total, parity))
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
