def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings

def row_winner(board):
    return any(winning_line(row) for row in board)

def column_winner(board):
    return row_winner(zip(*board))  # transpose to reuse row logic

def main_diagonal_winner(board):
    return winning_line([board[i][i] for i in range(len(board))])

def anti_diagonal_winner(board):
    return winning_line([board[i][len(board) - 1 - i] for i in range(len(board))])

def diagonal_winner(board):
    return main_diagonal_winner(board) or anti_diagonal_winner(board)

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    header = f'  {" ".join(str(i + 1) for i in range(size))}'
    return f'{header}\n{line.join(rows)}'

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins! ')

def print_draw():
    print("It's a draw! ")

def play_move(board, player):
    size = len(board)
    while True:
        try:
            print(f"{player}'s turn:")
            row = int(input(f"Enter row (1-{size}): ")) - 1
            col = int(input(f"Enter column (1-{size}): ")) - 1

            if 0 <= row < size and 0 <= col < size:
                if board[row][col] == ' ':
                    board[row][col] = player
                    print(format_board(board))
                    return
                else:
                    print("That cell is already taken. Try again.")
            else:
                print("Invalid input. Row and column must be within board size.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    
    total_moves = board_size * board_size
    players = [player1, player2]
    move_count = 0

    while move_count < total_moves:
        current_player = players[move_count % 2]
        play_move(board, current_player)
        move_count += 1

        if winner(board):
            print_winner(current_player)
            return

    print_draw()

# Start the game
play_game(3, 'X', 'O')