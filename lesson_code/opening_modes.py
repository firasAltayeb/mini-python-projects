import json

# gameBoard = {'1': ' ', '2': ' ', '3': ' ',
#              '4': ' ', '5': ' ', '6': ' ',
#              '7': ' ', '8': ' ', '9': ' '}

gameBoard = set({})
print(type(gameBoard))

# gameBoard = {}
# for i in range(9):
#     gameBoard[str(i)] = ''

gameBoard = {i: '' for i in range(9)}
print(type(gameBoard))

# for i in range(9):
#     with open('example.json', 'a+') as new_file:
#         if i == 0:
#             new_file.write('{\n')
#             new_file.write(f'\"{i}\":\"\",\n')
#         elif i != 0 and i != 8:
#             new_file.write(f'\"{i}\":\"\",\n')
#         elif i == 8:
#             new_file.write(f'\"{i}\":\"\"\n')
#             new_file.write('}')

# w Truncate file to zero length & open for writing (file created)
# w+ Truncate file to zero length & open for writing & reading (file created)
with open('example.txt', 'w') as new_file:
    print(gameBoard, file=new_file)

# a Open for writing at end (file created)
# a+ Open for reading and writing at start (file created)
with open('example.json', 'a+') as new_file:
    json.dump(gameBoard, new_file)
