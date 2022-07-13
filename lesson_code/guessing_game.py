import random


# ensures an integer is returned
def get_integer(message):
    while True:
        temp = input(message)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a number".format(temp))


guess = 0
lowest = 0
highest = 100
answer = random.randint(lowest, highest)

print("Please guess a number between {0} and {1}".format(lowest, highest))

while guess != answer:
    guess = get_integer("guess: ")

    if guess == answer:
        print("Well done you guessed right")
    else:        
        if guess < answer:
            print("Please guess higher")
        else: 
            print("Please guess lower")
