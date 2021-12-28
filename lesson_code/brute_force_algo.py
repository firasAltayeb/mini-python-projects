key_list = 'ab'
possibilities_list = []

for current in range(5):
    possibility = [i for i in key_list]
    for y in range(current):
        possibility = [x + i for i in key_list for x in possibility]
        print(possibility)
    possibilities_list = possibilities_list + possibility

print(possibilities_list)
