import random

possible_actions = ["rock", "paper", "scissors"]


def to_play_again(play_again):
    low_play_again = play_again.lower()
    if low_play_again == "y" or low_play_again == "yes":
        return True
    elif low_play_again == "n" or low_play_again == "no":
        return False
    else:
        print(f"{play_again} is not an option")
        again_play = input("Play again? (y/n): ")
        return to_play_again(again_play)


while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if not to_play_again(play_again):
        break
