parrot = "james's jackson"

letter = input('enter a character: ')

if letter in parrot:
    print('{} is in {}'.format(letter, parrot))
else:
    print('wrong letter')
