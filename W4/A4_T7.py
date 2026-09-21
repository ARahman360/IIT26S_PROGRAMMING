print("Program starting.")
print()

print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    result = 1
    temporary_number = number

    while temporary_number > 0:
        digit = temporary_number % 10
        result = result * digit
        temporary_number = temporary_number // 10

    print(str(number) + " -> " + str(result))

    number = result
    steps = steps + 1

if steps == 0:
    print("No more steps.")

print()
print("This program took " + str(steps) + " step(s)")

print()
print("Program ending.")