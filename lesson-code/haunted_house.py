import random

exits = ["north", "south", "east", "west"]

random_position = random.randint(0, len(exits))
correct_exit = exits[random_position]
attempt_counter = 0
choice = ""

welcome_box = """
welcome to Lily's haunted mansion.
In this game you are stuck in a hanuted mansion with one exit.
If you dont escape you DISSAPEAR >:)
"""

print(welcome_box)

while choice != correct_exit:
    choice = input("Please choose an exit: \n")

    attempt_counter = attempt_counter + 1
     
    if choice == correct_exit:
        print("YoU havE escAped")
    elif attempt_counter == 3:
        print("OH nO, YoU HaVe disSaPeaRrd")
        break
    else:
        print("oH noooOoo, yOur choIce was iNcorRect")

