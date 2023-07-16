gameBoard = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}


def print_board(dic):
    print(dic['1'] + '|' + dic['2'] + '|' + dic['3'])
    print('-+-+-')
    print(dic['4'] + '|' + dic['5'] + '|' + dic['6'])
    print('-+-+-')
    print(dic['7'] + '|' + dic['8'] + '|' + dic['9'])


def check_validity(choice):
    try:
        if 1 <= int(choice) <= 9:
            return True
        else:
            return False
    except:
        return False


def game():
    turn = 'X'
    count = 0
    winner_found = False

    while count < 9:
        print_board(gameBoard)
        print(f"It's {turn} turn. Move to which place?")

        move = input()
        while check_validity(move) is False:
            move = input(f"{move}'s is not a valid input. Please choose a number between 1-9:\n")

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                print_board(gameBoard)
                winner_found = True
                print(f" **** {turn} won. ****")
                break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    if count == 9 and winner_found is not True:
        print("It's a Tie!!")

    restart = input("Do want to play Again?(y/n):\n")
    if restart.casefold == "y".casefold:
        for key in gameBoard:
            gameBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
