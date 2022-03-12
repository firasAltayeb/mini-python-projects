gameBoard = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}


def printBoard(dic):
    print(dic['1'] + '|' + dic['2'] + '|' + dic['3'])
    print('-+-+-')
    print(dic['4'] + '|' + dic['5'] + '|' + dic['6'])
    print('-+-+-')
    print(dic['7'] + '|' + dic['8'] + '|' + dic['9'])


def game():
    turn = 'X'
    count = 0
    winner_found = False

    while count < 9:
        printBoard(gameBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                winner_found = True
                print(" **** " + turn + " won. ****")
                break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    if count == 9 and winner_found is not True:
        print("It's a Tie!!")

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in gameBoard:
            gameBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
