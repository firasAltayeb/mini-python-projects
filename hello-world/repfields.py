age = 24
print("my age is " + str(age) + " years")
print("my age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} day in Jan, Mar and May".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}"
      .format(28, 30, 31))

print()

print("""Jan: {2}, 
Feb: {0},
Mar: {2}, 
Apr: {1}, 
May: {2}""".format(28, 30, 31))
