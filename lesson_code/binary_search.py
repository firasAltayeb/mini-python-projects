def findValue(col, low, high, num_to_find):
    if low <= high:
        middle = low + (high - low) // 2

        if col[middle] == num_to_find:
            return middle
        elif col[middle] < num_to_find:
            low = middle + 1
            return findValue(col, low, high, num_to_find)
        else:
            high = middle - 1
            return findValue(col, low, high, num_to_find)
    else:
        return -1


lowest_index = 0
number_to_find = 22
collection = [7, 9, 14, 22, 34]

result_index = findValue(collection, lowest_index, len(collection) - 1, number_to_find)

if result_index == -1:
    print("This item was not found in the list")
else:
    print("The number {0} was found at index position {1}".format(number_to_find, result_index))
