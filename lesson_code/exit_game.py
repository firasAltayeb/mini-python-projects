available_exits = ["north", "south"]

exit_choice = ""
while exit_choice not in available_exits:
    exit_choice = input("please choose an exit: ").casefold()
    if exit_choice.casefold() == "quit":
        print("Game Over")
        break
    if exit_choice.casefold() in available_exits:
        print("you have escaped")
"""
else:
    print("you have escaped with else")
"""