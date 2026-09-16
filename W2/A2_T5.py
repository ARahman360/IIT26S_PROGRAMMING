word = str(input("Insert a closed compound word: "))

print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{word[-1]}'")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
ending = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

print(f"The word '{word}' sliced to the defined substring is '{word[start:ending:step]}'.")
print("Program ending.")
