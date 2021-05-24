panagram = """The quick brown
 for jumps\tover
 the lazy dog"""

words = panagram.split()
print(words)

number = "9,443,112,443,342,112"
print(number.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '6', '5', '6', ' ',
                  '7', '7', '5', ' ',
                  '6', '9', '9']

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)


integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)