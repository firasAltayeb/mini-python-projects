pangram = """The quick brown 
fox jumps over
the lazy dog
"""

words = pangram.split()
print(words)

number = "9,834,000,000"
print(number.split(","))

dog_breeds = ["Husky", "Shiba", "Spitz", "Shepherd",
              "Pug", "Maltese", "Terrier"]

separator = ", "
output = separator.join(dog_breeds)
print(output)

print("/ ".join(["Munchikin", "Ragdoll", "Bengal", "American Bobtail"]))

values = ''
for index in range(len(dog_breeds)):
    values += dog_breeds[index] + ' '

print(values)

first_index_values = []
for value in dog_breeds:
    first_index_values.append(values.index(value))

print(first_index_values)
