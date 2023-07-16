age = int(input("how old are you? \n"))

# if 16 <= age <= 65:
if age in range(16, 66):
    print("you can work")
else:
    print("play video games")

print('*' * 10)

if age < 16 or age > 65:
    print("play video games")
else:
    print('you can work')

