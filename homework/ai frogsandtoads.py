import sys
import time


n = int(sys.argv[1])

toads = ['T'] * n
frogs = ['F'] * n
board = toads + [''] + frogs

total_count = 0
solution_found = False



# Recursive move function
def move(board, depth):
    global total_count, solution_found
    time.sleep(.1)
    move_made = False

    if board == ['F'] * n + [''] + ['T'] * n:
        print(f"Solution found!!!")
        solution_found = True
        return

    for x in range(len(board)):
        if solution_found:
            return

        # Check if toad can jump 1 spot
        if x + 1 < len(board) and board[x] == 'T' and board[x + 1] == '':
            board_copy = board.copy()
            board_copy[x] = ''
            board_copy[x + 1] = 'T'
            total_count += 1
            print(total_count, depth, board_copy)
            move_made = True
            move(board_copy, depth + 1)

        # Check if toad jump can jump 2 spaces
        elif x + 2 < len(board) and board[x] == 'T' and board[x + 1] == 'F' and board[x + 2] == '':
            board_copy = board.copy()
            board_copy[x], board_copy[x + 2] = '', 'T'
            total_count += 1
            print(total_count, depth, board_copy)
            move_made = True
            move(board_copy, depth + 1)

        # Check if frog can jump 1 space left
        elif x - 1 >= 0 and board[x] == 'F' and board[x - 1] == '':
            board_copy = board.copy()
            board_copy[x], board_copy[x - 1] = '', 'F'
            total_count += 1
            print(total_count, depth, board_copy)
            move_made = True
            move(board_copy, depth + 1)


        elif x - 2 >= 0 and board[x] == 'F' and board[x - 1] == 'T' and board[x - 2] == '':
            board_copy = board.copy()
            board_copy[x], board_copy[x - 2] = '', 'F'
            total_count += 1
            print(total_count, depth, board_copy)
            move_made = True
            move(board_copy, depth + 1)



# Start the game
print(f"Starting Board: {board}")
move(board, 1)