letters = ("a", "b", "c", "d")
print(letters)
print(letters[0])
print(letters[1])

#this wont work becuase tuples are immutable
#letters[0] = "a2"

letters2 = list(letters)
print(letters2)

letters2[0] = "a2"
print(letters2)