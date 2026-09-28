def main():
    print("Program starting.")
    print("This program can copy a file.")
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")

    print("Reading file '" + source + "' content.")
    file = open(source, "r")
    content = file.read()
    file.close()
    print("File content ready in memory.")

    print("Writing content into file '" + destination + "'.")
    file = open(destination, "w")
    file.write(content)
    file.close()

    print("Copying operation complete.")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
