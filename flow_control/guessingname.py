import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        break
    if guess == answer:
        print("correct guess - first shot")
        break
    else:
        if guess < answer:
            print("Please higher")
        else:
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("You guessed correctly")
            break
