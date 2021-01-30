answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("smart boy")
else:
    if guess < answer:
        print("Please higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("good boy")
    else:
        print("bad boy")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Guessed right")
#     else:
#         print("wrong")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Guessed right")
#         print("wrong")
# else:
#     print("You got it first time")


