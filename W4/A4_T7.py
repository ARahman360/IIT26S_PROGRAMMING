print("Program starting.")
print()

print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = str(number)
    result = 1

    for digit in digits:
        result = result * int(digit)

    print(" * ".join(digits) + " = " + str(result))
    number = result
    steps = steps + 1

print("No more steps.")
print()
print("This program took " + str(steps) + " step(s)")
print()
print("Program ending.")
