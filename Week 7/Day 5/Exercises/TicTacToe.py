board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
]


def display_board():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-+-+-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-+-+-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}\n")


def player_input(player):
    print(f"Player {player}'s' Turn...\n")
    while True:
        row = int(input("Enter row:(0,1 or 2) "))
        colmun = int(input("Enter colmun:(0,1 or 2) "))
        if board[row][colmun] == ' ':
            board[row][colmun] = player
            break
        else:
            print("The square is already taken,try another one")
    display_board()


def check_win():
    if board[0][0] == board[0][1] == board[0][2] != ' ':  # across the top
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][0] + " won. ****")
        return True
    elif board[1][0] == board[1][1] == board[1][2] != ' ':  # across the middle
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[1][0] + " won. ****")
        return True
    elif board[2][0] == board[2][1] == board[2][2] != ' ':  # across the bottom
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[2][0] + " won. ****")
        return True
    elif board[0][0] == board[1][0] == board[2][0] != ' ':  # down the left side
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][0] + " won. ****")
        return True
    elif board[0][1] == board[1][1] == board[2][1] != ' ':  # down the middle
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][1] + " won. ****")
        return True
    elif board[0][2] == board[1][2] == board[2][2] != ' ':  # down the right side
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][2] + " won. ****")
        return True
    elif board[0][0] == board[1][1] == board[2][2] != ' ':  # diagonal
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][0] + " won. ****")
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':  # diagonal
        display_board()
        print("\nGame Over.\n")
        print(" **** " + board[0][2] + " won. ****")
        return True


def play():
    print("Welcome to TIC TAC TOE")
    display_board()
    player = 'X'
    turn_number = 1
    while turn_number < 10:
        player_input(player)
        if turn_number >= 5:
            if check_win() == True:
                break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        turn_number += 1
    if turn_number == 10:
        print("\nGame Over.\n")
        print("It's a Tie!!")


play()
