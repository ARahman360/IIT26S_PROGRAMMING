########################################################
# Task A9_T5
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def askColor(PName: str) -> int:
    value = int(input("Insert {}: ".format(PName)))
    if value < 0 or value > 255:
        raise ValueError("Color is out of range.")
    return value


def main() -> None:
    print("Program starting.")
    try:
        red = askColor("red")
        green = askColor("green")
        blue = askColor("blue")
    except ValueError:
        print("Couldn't perform the designed task due to the invalid input values.")
    else:
        print("RGB Details:")
        print("- Red {}".format(red))
        print("- Green {}".format(green))
        print("- Blue {}".format(blue))
        print("- Hex #{:02x}{:02x}{:02x}".format(red, green, blue))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
