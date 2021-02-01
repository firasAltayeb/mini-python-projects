choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("please choose")
        print("1:\t dance")
        print("2:\t eat")
        print("3:\t sleep")
        print("0:\tExit \n")

    choice = input()
