print("Program starting.")
print()

starting_value = int(input("Insert starting value: "))
stopping_value = int(input("Insert stopping value: "))

print()
print("Starting while-loop:")

number = starting_value

while number <= stopping_value:
    if number == stopping_value:
        print(number)
    else:
        print(number, end=" ")

    number = number + 1

print()
print()
print("Program ending.")