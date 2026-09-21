print("Program starting.")
print()

starting_value = int(input("Insert starting value: "))
stopping_value = int(input("Insert stopping value: "))

print()
print("Starting for-loop:")

for number in range(starting_value, stopping_value + 1):
    if number == stopping_value:
        print(number)
    else:
        print(number, end=" ")

print()

print("Program ending.")