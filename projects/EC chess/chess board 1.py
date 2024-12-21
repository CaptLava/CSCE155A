import numpy as np

# Global Variables
LIMIT = 20
FOUND = False
min_depth = float('inf')  # Smallest depth for the solution
solution = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
past_arrays = []  # To store visited states
solution_path = []  # To track the steps of the solution


def valid_moves(board):
    """Generate all valid moves for the blank space."""
    moves = []
    # Find the position of 0 (blank space)
    x, y = np.where(board == 0)
    x, y = x[0], y[0]

    # Possible moves: (dx, dy)
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Ensure move is within bounds
            new_board = board.copy()
            new_board[x, y], new_board[nx, ny] = new_board[nx, ny], new_board[x, y]
            moves.append(new_board)

    return moves


def move(board, depth):
    """Recursive function to solve the puzzle."""
    global FOUND, min_depth, past_arrays, solution_path

    # Stop recursion if depth exceeds the limit
    if depth > LIMIT:
        return False

    # Check if solution is found
    if np.array_equal(board, solution):
        if depth < min_depth:  # Check for quicker solution
            FOUND = True
            min_depth = depth
            solution_path = [board.copy()]  # Start tracking the solution path
        return True

    # Avoid revisiting states
    for past_board in past_arrays:
        if np.array_equal(board, past_board):
            return False

    # Mark this board as visited
    past_arrays.append(board.copy())

    # Explore all valid moves
    for next_board in valid_moves(board):
        if move(next_board, depth + 1):
            # If solution found, add this step to the solution path
            if FOUND:
                solution_path.append(board.copy())
            return True

    # Backtrack: remove current board from visited (optional for DFS)
    past_arrays.pop()
    return False


def main():
    # Initial board state
    start_board = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])

    # Start solving
    move(start_board, 0)

    if FOUND:
        print("Solved in {} moves:".format(min_depth))
        for step in reversed(solution_path):  # Print in correct order
            print(step)
    else:
        print("No solution found within the depth limit.")


if __name__ == "__main__":
    main()
