def main() -> None:
    numbers: list[int] = []
    print("Program starting.")
    print("Collect positive integers.")
    while True:
        number = int(input("Insert positive integer(negative stops): "))
        if number < 0:
            break
        if number > 0:
            numbers.append(number)
    print("Stopped collecting positive integers.")
    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print("Displaying {} integers:".format(len(numbers)))
        for index in range(len(numbers)):
            print("- Index {} => Ordinal {} => Integer {}".format(index, index + 1, numbers[index]))
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
