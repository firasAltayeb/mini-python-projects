import random

all_exits = ["north", "south", "east", "west", "up", "down", "left", "right"]
opposite_exit = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east',
                 'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', }

random_index = random.randrange(len(all_exits))
correct_exit = all_exits[random_index]
attempt_counter = 0
exit_choice = ""

print("You are stuck in a haunted house with one exit. If you don't escape, you're in big trouble.")

while exit_choice.casefold() != correct_exit:
    if attempt_counter >= 3:
        hint_choice = input("Would you like a hint: ")
        if hint_choice.casefold() == 'yes':
            print(f"Opposite direction of {opposite_exit[correct_exit]}")

    exit_choice = input("Please choose an exit: ")
    # Code below changes the exit everytime to increase difficulty
    # random_index = random.randrange(len(all_exits))
    # correct_exit = all_exits[random_index]
    if exit_choice.casefold() == correct_exit:
        print("You have escaped")
    if exit_choice.casefold() == "quit":
        print("Game Over")
        break

    attempt_counter += 1

# else:
#     print("you have escaped with else")
