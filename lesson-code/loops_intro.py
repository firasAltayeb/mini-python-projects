i = 0
while i < 10:
    print("I is now " + str(i))
    i = i + 1

parrot = "jame's jackson"

for character in parrot:
    print(character)

for i in range(10, 0, -2):
    print("i is now {}".format(i))

for i in range(1, 20, 4):
    print("i is now {}".format(i))

for i in range(5):
    print("i is now {}".format(i))

name = input('please enter your name: ')
# if name:
if name != '':
    print('Hello, {}'.format(name))
else:
    print('do you have no name')

for x in range(0, 10):
    for y in range(0, 3):
        print("The current outer for loop cycle is {0} ".format(x) +
              "and the current inner for loop cycle is {0} ".format(y))
