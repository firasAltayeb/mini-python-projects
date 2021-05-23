parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,432;432:543 534,780"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators
                 else " " for char in number).split()
print([int(val) for val in values])

print()

print(parrot)
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[:9])
print(parrot[10:])
print(parrot[:])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[-14])
