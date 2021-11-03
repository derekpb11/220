"""
Name: Derek Bolch
lab10.py
"""


def build():
    board_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_nums


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], "|", board[n+1], "|", board[n+2])


def place(board, pos, piece):
    if piece == "X" or piece == "O":
        board[pos-1] = piece


def legal(board, pos):
    if pos-1 >= 0 and pos-1 <= 8 and (board[pos-1] != "X" or board[pos-1] != "O"):
        return True
    return False


def is_won(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True

    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True

    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True

    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True

    return False


def over(board):
    if is_won(board, "X"):
        return True
    elif is_won(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()
    while True:
        display(board)
        x_input = eval(input("Input move for player X: "))
        while not legal(board, x_input):
            x_input = eval(input("Input move for player X: "))
        place(board, x_input, "X")

        if over(board):
            if is_won(board, "X"):
                print("X won")
                break
            elif is_won(board, "O"):
                print("O won")
                break
            else:
                print("The game is a tie")
                break

        display(board)
        O_input = eval(input("Input move for player O: "))
        while not legal(board, O_input):
            O_input = eval(input("Input move for player O: "))
        place(board, O_input, "O")

        if over(board):
            if is_won(board, "X"):
                print("X won")
                break
            elif is_won(board, "O"):
                print("O won")
                break
            else:
                print("The game is a tie")
                break


play()
