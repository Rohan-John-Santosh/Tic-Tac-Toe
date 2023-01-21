def draw(squares):
    board = (f"|{squares[1]}|{squares[2]}|{squares[3]}|\n"
             f"|{squares[4]}|{squares[5]}|{squares[6]}|\n"
             f"|{squares[7]}|{squares[8]}|{squares[9]}|")
    print(board)


def check(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def win(squares):
    # Horizontal Cases
    if (squares[1] == squares[2] == squares[3]) \
        or (squares[4] == squares[5] == squares[6]) \
            or (squares[7] == squares[8] == squares[9]):
        return True
    # Vertical Cases
    elif (squares[1] == squares[4] == squares[7]) \
        or (squares[2] == squares[5] == squares[8]) \
            or (squares[3] == squares[6] == squares[9]):
        return True
    # Diagonal Cases
    elif (squares[1] == squares[5] == squares[9]) \
            or (squares[3] == squares[5] == squares[7]):
        return True
    else:
        return False
