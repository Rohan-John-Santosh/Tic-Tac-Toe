from Helper import draw, check, win
import os

squares = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

start = True
finish = False
turn = 0
prev_turn = -1
while start:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(squares)
    if prev_turn == turn:
        print("Invalid square selected, please pick another.")
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your square or press z to quit")
    # Get input from the player
    choice = input()
    if choice == 'z':
        start = False
    # Check if player inputs a value from 1-9
    elif str.isdigit(choice) and int(choice) in squares:
        # Check if the square has already been occupied
        if not squares[int(choice)] in ["X", "O"]:
            # Valid Input, update the board
            turn += 1
            squares[int(choice)] = check(turn)
    # Check if game has ended
    if win(squares):
        start, finish = False, True
        if turn > 8:
            start = False

os.system('cls' if os.name == 'nt' else 'clear')
draw(squares)
if finish:
    if check(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("Tie!")

print("Thanks for playing!")
