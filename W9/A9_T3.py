########################################################
# Task A9_T3
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import sys


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print('Error! File "{}" does not exist.'.format(filename))
        sys.exit(1)

    print("## {} ##".format(filename))
    print(content, end="")
    if content != "" and not content.endswith("\n"):
        print()
    print("## {} ##".format(filename))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
