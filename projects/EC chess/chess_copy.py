import numpy as np, csv as c, sys as s
import math
import time

# initialize the board
S = 4
board = np.full((S, S), ' ')
solution = np.full((S, S), ' ')

# Setting global variables
LIMIT = 20  # limiting the maximum depth
FOUND = False  # Set to true when solution is found


# reading the file
def fileAccess(filename):
    result = []
    i = 0
    print('Opening file ', filename)
    with open(filename) as inFile:  # create file object
        print('Reading ', filename)
        for x in list(c.reader(inFile, delimiter=',')):
            result.append(x)
        print('Closing ', filename)
    inFile.close()  # close the file
    return result


def move(board, solution, depth, best_depth):
    global LIMIT, FOUND, past_arrays

    ### Force Unwinding to Reveal Solution
    if FOUND == True:
        return




    ### Check if previous state visited already at more optimal depth, if yes change the flag to 1.

    flag = 0
    if depth ==0:
        past_arrays = []
    for i in range(len(past_arrays)):
        if board == past_arrays[i]:
            flag = 1
            past_arrays.append(board)
            past_arrays[i].append(depth)
            if depth > past_arrays[i,1]:
                move(past_arrays[i,0], solution, depth + 1, best_depth)

    if (depth == LIMIT or flag == 1):
        return

    if (np.array_equal(board, solution)):

        FOUND = True
        print()

        print("Step: %d" % depth)
        print(board)
        return

    # Now you complete the recursive function to fill out to move your knights and check if the optimal solution is reached. If you do not check for optimality your code will be executing for hours without finding the solution.
    for x in range(len((board))):
        for y in range(len((board))):
            if board[x,y] == 'W':
                knight_location = [x,y]
                break

    if knight_location == [3,0]:
        board_copy = board.copy()
        board_copy[knight_location[0],knight_location[1]] = ' '
        board_copy[1,1] = 'W'
        move(board_copy, solution, depth+1, best_depth)

    if knight_location == [1,1]:
        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy[3,2] = 'W'
        move(board_copy, solution, depth + 1, best_depth)

        # checks other move, fine because of best depth check
        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy[3, 0] = 'W'
        move(board_copy, solution, depth + 1, best_depth)




    if knight_location == [3,2]:
        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy [1,3] = 'W'
        move(board_copy, solution, depth + 1, best_depth)

        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy[1, 1] = 'W'
        move(board_copy, solution, depth + 1, best_depth)

    if knight_location == [1,3]:
        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy[0,1] = 'W'
        move(board_copy, solution, depth + 1, best_depth)

        board_copy = board.copy()
        board_copy[knight_location[0], knight_location[1]] = ' '
        board_copy[3,2] = 'W'
        move(board_copy, solution, depth + 1, best_depth)










    # Here you finish your coding
    if FOUND == True:
        print("Step: %d" % depth)
        print(board)


inFile = s.argv[1]
myList = fileAccess(inFile)

board[0] = myList[0]
board[1] = myList[1]
board[2] = myList[2]
board[3] = myList[3]
solution[0] = myList[5]
solution[1] = myList[6]
solution[2] = myList[7]
solution[3] = myList[8]

move(board, solution, 0, 0)

