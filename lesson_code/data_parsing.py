import json

# gameBoard = {'1': ' ', '2': ' ', '3': ' ',
#              '4': ' ', '5': ' ', '6': ' ',
#              '7': ' ', '8': ' ', '9': ' '}

gameBoard = set({})
print(type(gameBoard))

gameBoard = {}
print(type(gameBoard))

for i in range(9):
    gameBoard[str(i)] = ''

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

with open('example.json', 'a+') as new_file:
    json.dump(gameBoard, new_file)
