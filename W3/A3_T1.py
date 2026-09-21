
print("Program starting.")

print("Insert two integers.")

first_integer = int(input("Insert first integer: "))
second_integer = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if first_integer > second_integer:
    print("First integer is greater.")
elif second_integer > first_integer:
    print("Second integer is greater.")
else:
    print("Integers are the same.")

print("Adding integers together")

sum_of_integers = first_integer + second_integer

print(first_integer, "+", second_integer, "=", sum_of_integers)

print("Checking the parity of the sum...")

if sum_of_integers % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")

