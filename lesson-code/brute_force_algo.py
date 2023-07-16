possible_keys = "ab"
password_length = 3
list_of_possibilities = []

for j in range(password_length):
    # reverts possibility to original state
    possibility = [i for i in possible_keys]
    print("j cycle #{}".format(j))
    j == 0 and print("possibility is now {}".format(possibility))
    for k in range(j):
        print("k cycle #{}".format(k))
        possibility = [x + y for x in possibility for y in possible_keys]
        print("possibility is now {}".format(possibility))
    list_of_possibilities.append(possibility)
    print("above possibility is added to the list_of_possibilities")

print(list_of_possibilities)

# possibility = []
# for i in possible_keys:
#     possibility.append(i)
#     print(possibility)
#
# for x in possible_keys:
#     print("x is {}".format(x))
#     for i in possible_keys:
#         print("i is {}".format(i))
#         possibility.append(x+i)
#         print(possibility)
