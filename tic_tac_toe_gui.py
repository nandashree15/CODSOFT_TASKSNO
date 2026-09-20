import tkinter as tk
from tkinter import messagebox
import math

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("420x520")
root.resizable(False, False)

# Game variables
board = [""] * 9
human = "X"
ai = "O"
game_over = False

# Winning combinations
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


# Check whether a player has won
def check_winner(player):
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


# Check whether the board is full
def board_full():
    return all(cell != "" for cell in board)


# Minimax algorithm
def minimax(is_maximizing):
    if check_winner(ai):
        return 1

    if check_winner(human):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = ai
                score = minimax(False)
                board[i] = ""
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = human
                score = minimax(True)
                board[i] = ""
                best_score = min(best_score, score)

        return best_score


# Find the best move for AI
def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(False)
            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = ai
        buttons[best_move].config(text=ai)
        check_game_end()


# Handle player's move
def player_move(index):
    global game_over

    if game_over or board[index] != "":
        return

    board[index] = human
    buttons[index].config(text=human)

    if check_game_end():
        return

    status_label.config(text="AI is thinking...")

    root.after(400, ai_move)


# Check win or draw
def check_game_end():
    global game_over

    if check_winner(human):
        game_over = True
        status_label.config(text="You win!")
        messagebox.showinfo("Game Over", "You won!")
        new_game()
        return True

    if check_winner(ai):
        game_over = True
        status_label.config(text="AI wins!")
        messagebox.showinfo("Game Over", "AI won!")
        new_game()
        return True

    if board_full():
        game_over = True
        status_label.config(text="It's a draw!")
        messagebox.showinfo("Game Over", "It's a draw!")
        new_game()
        return True

    status_label.config(text="Your turn (X)")
    return False


# Start a new game
def new_game():
    global board, game_over

    board = [""] * 9
    game_over = False

    for button in buttons:
        button.config(text="")

    status_label.config(text="Your turn (X)")


# Title
title_label = tk.Label(
    root,
    text="Tic-Tac-Toe",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=15)


# Status
status_label = tk.Label(
    root,
    text="Your turn (X)",
    font=("Arial", 14)
)
status_label.pack(pady=5)


# Game board
board_frame = tk.Frame(root)
board_frame.pack(pady=15)

buttons = []

for i in range(9):
    button = tk.Button(
        board_frame,
        text="",
        font=("Arial", 30, "bold"),
        width=4,
        height=2,
        command=lambda index=i: player_move(index)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=2,
        pady=2
    )

    buttons.append(button)


# New Game button
new_game_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14, "bold"),
    command=new_game
)

new_game_button.pack(pady=15)


# Start the application
root.mainloop()