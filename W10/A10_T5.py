########################################################
# Task A10_T5
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def recursiveFactorial(PNum: int) -> int:
    if PNum < 0:
        raise ValueError("Factorial cannot be calculated for negative numbers.")
    if PNum == 0 or PNum == 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    number = int(input("Insert factorial: "))
    if number < 0:
        print("Factorial cannot be calculated for negative numbers.")
    else:
        result = recursiveFactorial(number)
        print("Factorial {}!".format(number))
        factors = []
        for value in range(number, 0, -1):
            factors.append(str(value))
        if number == 0:
            factors.append("0")
        print("{} = {}".format(" * ".join(factors), result))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
