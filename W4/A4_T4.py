print("Program starting.")
print()

word_count = 0
character_count = 0

word = input("Insert word (empty stops): ")

while word != "":
    word_count = word_count + 1
    character_count = character_count + len(word)

    word = input("Insert word (empty stops): ")

print()
print("You inserted:")
print("- " + str(word_count) + " words")
print("- " + str(character_count) + " characters")

print()
print("Program ending.")