def findValue(num, low, high, num_to_find):
    if low <= high:
        middle = low + (high - low) // 2

        if num[middle] == num_to_find:
            return middle
        elif num[middle] < num_to_find:
            low = middle + 1
            return findValue(num, low, high, num_to_find)
        else:
            high = middle - 1
            return findValue(num, low, high, num_to_find)
    else:
        return -1


numbers = [7, 9, 14, 22, 34]
number_to_find = 22

result_index = findValue(numbers, 0, len(numbers) - 1, number_to_find)

if result_index == -1:
    print("This item was not found in the list")
else:
    print("The number {0} was found at index position {1}".format(number_to_find, result_index))
