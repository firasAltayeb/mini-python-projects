empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even , odd]
print(numbers)

for number_list in numbers:
    print(number_list)


"""
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

# print(min(even))
# print(max(odd))
# print(min(even))
# print(max(odd))
#
# print()
#
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("s"))
"""