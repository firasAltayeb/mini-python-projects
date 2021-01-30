number = input("Please enter a series of numbers using separators ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char not in separators
                 else " " for char in number).split()
print(sum([int(val) for val in values]))
