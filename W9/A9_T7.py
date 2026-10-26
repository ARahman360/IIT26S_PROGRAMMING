########################################################
# Task A9_T7
# Developer First_name Last_name
# Date 2026-10-26
########################################################

import os
import sys


def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Usage: python A9_T7.py source_file destination_file")
    return None


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True
    print('Source file "{}"'.format(PSrcFile))
    print('Destination file "{}"'.format(PDstFile))

    if os.path.exists(PDstFile):
        answer = input("Destination file exists. Overwrite (y/n)?: ")
        if answer.lower() != "y":
            proceed = False

    if proceed:
        try:
            with open(PSrcFile, "r", encoding="utf-8") as source:
                text = source.read()
            with open(PDstFile, "w", encoding="utf-8") as destination:
                destination.write(text)
            print('Copying file "{}" to "{}".'.format(PSrcFile, PDstFile))
        except OSError as error:
            print("Error! {}".format(error))
            sys.exit(-1)
    else:
        print("Copy cancelled.")
    return None


def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        showHelp()
    else:
        source_file = sys.argv[1]
        destination_file = sys.argv[2]
        copyFile(source_file, destination_file)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
