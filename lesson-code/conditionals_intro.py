name = input('please enter your name: ')
# if name:
if name != '':
    print('Hello, {}'.format(name))
else:
    print('do you have no name')

age = int(input("how old are you? \n"))

# if 16 <= age <= 65:
if age in range(16, 66):
    print("you can work")
elif age in range(0, 6):
    print("You are too young")
else:
    print("play video games")

print('*' * 10)

if age < 16 or age > 65:
    print("play video games")
else:
    print('you can work')

