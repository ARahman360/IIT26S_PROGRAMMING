def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")

    file = open(filename, "r")
    content = file.read()
    file.close()

    print('#### START "' + filename + '" ####')
    print(content, end="")
    print()
    print('#### END "' + filename + '" ####')
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
