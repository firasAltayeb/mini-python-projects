from random import randint

def update_points(points, dice_value):
    if dice_value == 1:
        return 0
    else:
        return points + dice_value

def display_board():
    print()
    print (":) smiley " * 10)
    print (f"{player_1_name} score is: {player_1_points}")
    print (f"{player_2_name} score is: {player_2_points}")
    print (":) " * 20)
    print()


welcome_box = """
welcome to Lily's dice game.
In this game you and your friend roll a 6 sided dice each round.
The player gets the value of the dice added to their points.
If the player rolled a 1 all their points go to 0 >:) evil
The first player to reach 30 points win! :)
"""
print(welcome_box)

player_1_points = 0
player_2_points = 0

player_1_name = input("what is player 1 name? \n")
while player_1_name == "":
    player_1_name = input("what is player 1 name? \n")   
print(f"hello {player_1_name} :) \n")

player_2_name = input("what is player 2 name? \n")
while player_2_name == "":
    player_2_name = input("what is player 2 name? \n")
print(f"hello {player_2_name} :) \n")

turn_round = 1

while True:
    if turn_round % 2:
        input(f"{player_1_name} press enter to roll the dice: ")
 
        dice_1_value = randint (1,6)
        player_1_points = update_points(player_1_points, dice_1_value)
            
        display_board()

        if player_1_points >= 30:
            print(f"{player_1_name} wins !")
            break
    else:
        input(f"{player_2_name} press enter to roll the dice: ") 

        dice_2_value = randint (1,6)
        player_2_points = update_points(player_2_points, dice_2_value)

        display_board()

        if player_2_points >= 30:
            print(f"{player_2_name} wins !")
            break

    turn_round = turn_round + 1;

