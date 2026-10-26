########################################################
# Task A9_T4
# Developer First_name Last_name
# Date 2026-10-26
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    celsius = float(feed)
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(celsius))
    return celsius


def main() -> None:
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print("You inserted {} °C".format(celsius))
    except ValueError as error:
        print("Error! {}".format(error))
    except Exception as error:
        print("Error! {}".format(error))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
