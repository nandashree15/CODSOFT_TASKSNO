print("=" * 40)
print("       TIC-TAC-TOE AI")
print("=" * 40)
print("You are X | AI is O")
print()

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move in range(9) and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Please choose an empty position.")

        except ValueError:
            print("Please enter a number from 1 to 9.")
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for move in range(9):
            if board[move] == " ":
                board[move] = "O"

                score = minimax(False)

                board[move] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in range(9):
            if board[move] == " ":
                board[move] = "X"

                score = minimax(True)

                board[move] = " "

                best_score = min(best_score, score)

        return best_score


def ai_move():

    best_score = -float("inf")
    best_move = None

    for move in range(9):

        if board[move] == " ":

            board[move] = "O"

            score = minimax(False)

            board[move] = " "

            if score > best_score:
                best_score = score
                best_move = move

    board[best_move] = "O"

    print("AI chose position", best_move + 1)
def play_game():

    while True:
        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("You won!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break


while True:

    play_game()

    again = input("Do you want to play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]