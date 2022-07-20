import random


# ensures an integer is returned
def get_integer(message):
    while True:
        temp = input(message)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f"{temp} is not a number")
            return get_integer(message)


# def get_integer(message):
#     while True:
#         temp = input(message)
#         if temp.isnumeric():
#             return int(temp)
#         else:
#             print(f"{temp} is not a number")


guess = 0
lowest = 0
highest = 100
number_of_guesses = 0
answer = random.randint(lowest, highest)

print(f"Please guess a number between {lowest} and {highest}")

while guess != answer:
    # below minimize bugs from edge cases
    # guess = get_integer("guess: ")
    guess = int(input("guess: "))
    number_of_guesses += 1

    if guess == answer:
        print("Well done you guessed right")
        print(f"{number_of_guesses} guesses were attempted")
    else:        
        if guess < answer:
            print("Please guess higher")
        else: 
            print("Please guess lower")
