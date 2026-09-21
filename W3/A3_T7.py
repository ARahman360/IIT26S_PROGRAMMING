print("Program starting.")
print("Testing decision structures.")

value = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice = input("Your choice: ")

if choice == "1":
    print("Using one multi-branched decision structure.")

    result = value

    if result >= 400:
        result = result + 44
    elif result >= 200:
        result = result + 22
    elif result >= 100:
        result = result + 11

    print("Result is " + str(result))

elif choice == "2":
    print("Using multiple independent if-statements.")

    result = value

    if result >= 400:
        result = result + 44

    if result >= 200:
        result = result + 22

    if result >= 100:
        result = result + 11

    print("Result is " + str(result))

elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")