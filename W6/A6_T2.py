def main():
    print("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    filename = input("Insert filename: ")

    file = open(filename, "w")
    file.write(firstName + "\n")
    file.write(lastName + "\n")
    file.close()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
