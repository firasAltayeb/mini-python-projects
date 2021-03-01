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

metallica = "Ride the lighting", "Metallica", 1984
title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffe table", 200, 100, 75, 34.5)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)


