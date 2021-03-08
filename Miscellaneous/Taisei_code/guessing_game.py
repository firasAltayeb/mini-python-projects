import random

guess = 0
highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))

def get_integer(message):
    while True:
        temp = input(message)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a number".format(temp))

while guess != answer:
    guess = get_integer("guess: ")

    if guess == answer:
        print("Well done you guessed right")
    else:        
        if guess < answer:
            print("Please guess higher")
        else: 
            print("Please guess lower")