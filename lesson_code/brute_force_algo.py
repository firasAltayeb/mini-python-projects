possible_keys = "ab"
password_length = 2
list_of_possibilities = []

for w in range(password_length):
    possibility = [i for i in possible_keys]
    print("w cycle: {}".format(w))
    for y in range(w):
        print("y cycle: {}".format(y))
        possibility = [x + i for x in possibility for i in possible_keys]
        # print(possibility)
    list_of_possibilities.append(possibility)

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
