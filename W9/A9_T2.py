########################################################
# Task A9_T2
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import sys


def main() -> None:
    print("Program starting.")
    feed = input("Insert exit code(0-255): ")

    try:
        code = int(feed)
    except ValueError:
        print("Invalid exit code.")
        sys.exit(1)

    if code < 0 or code > 255:
        print("Invalid exit code.")
        sys.exit(1)

    if code == 0:
        print("Clean exit")
    else:
        print("Error exit")
    sys.exit(code)


if __name__ == "__main__":
    main()
