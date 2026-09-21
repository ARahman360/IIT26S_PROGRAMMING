print("Program starting.")

print()
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = input("Your choice: ")

if choice == "1":
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(str(round(celsius, 1)) + " °C equals to " + str(round(fahrenheit, 1)) + " °F")
elif choice == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(str(round(fahrenheit, 1)) + " °F equals to " + str(round(celsius, 1)) + " °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")