def minimal_number_of_packages(items, available_large_packages,
                               available_small_packages):
    remaining_items = items
    large_used_counter = 0
    small_used_counter = 0
    enough_packages = 0

    for i in range(available_large_packages):
        if remaining_items == 0:
            break
        else:
            remaining_items -= 5
            large_used_counter += 1

    if remaining_items != 0:
        for i in range(available_small_packages):
            if remaining_items == 0:
                break
            else:
                remaining_items -= 1
                small_used_counter += 1

    if remaining_items > 0:
        enough_packages = -1
    else:
        enough_packages = large_used_counter + small_used_counter

    return enough_packages


print(minimal_number_of_packages(16, 2, 10))
print(minimal_number_of_packages(10, 2, 0))
print(minimal_number_of_packages(10, 0, 10))
print(minimal_number_of_packages(10, 0, 9))
print(minimal_number_of_packages(10, 1, 4))
print(minimal_number_of_packages(10, 1, 0))
