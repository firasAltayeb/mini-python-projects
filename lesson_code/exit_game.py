import random

all_exits = ["north", "south", "east", "west", "up", "down", "left", "right"]
available_exits = ["north"]

exit_choice = ""
while exit_choice not in available_exits:
    # exit_choice = input("Please choose an exit: ")
    # random_index = random.randint(0, len(all_exits)-1)
    random_index = random.randrange(len(all_exits))
    exit_choice = all_exits[random_index]
    print(exit_choice)
    if exit_choice.casefold() in available_exits:
        print("You have escaped")
    if exit_choice == "quit":
        print("Game Over")
        break

"""
else:
    print("you have escaped with else")
"""