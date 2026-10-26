########################################################
# Task A9_T1
# Developer First_name Last_name
# Date 2026-10-26
########################################################


def main() -> None:
    total = 0.0
    print("Program starting.")
    print()

    while True:
        feed = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(feed)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(feed))
            continue

        if value == 0:
            break
        total += value

    print()
    print("Final sum is {:.2f}".format(total))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
