import random

all_exits = ["north", "south", "east", "west", "up", "down", "left", "right"]

random_index = random.randrange(len(all_exits))
correct_exit = all_exits[random_index]
exit_choice = ""

while exit_choice.casefold() != correct_exit:
    exit_choice = input("Please choose an exit: ")
    # random_index = random.randrange(len(all_exits))
    # correct_exit = all_exits[random_index]
    if exit_choice.casefold() == correct_exit:
        print("You have escaped")
    if exit_choice.casefold() == "quit":
        print("Game Over")
        break

"""
else:
    print("you have escaped with else")
"""