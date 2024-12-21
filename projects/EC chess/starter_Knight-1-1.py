import numpy as np, csv as c, sys as s
import math
import time

#initialize the board
S = 4
board = np.full((S,S),' ')
solution = np.full((S,S),' ')

#Setting global variables 
LIMIT = 20 #limiting the maximum depth
FOUND = False #Set to true when solution is found

#reading the file
def fileAccess (filename):
	result =  []
	i = 0
	print('Opening file ', filename)
	with open(filename) as inFile: # create file object
		print('Reading ', filename)
		for x in list(c.reader(inFile, delimiter= ',')):  
			result.append(x)
		print('Closing ', filename)
	inFile.close()  # close the file
	return result

def move(board, solution, depth):
	global LIMIT, FOUND

	### Force Unwinding to Reveal Solution
	if FOUND == True:
		return

	print("Depth: %d" % depth)
	print(board)

	### Check if previous state visited already at more optimal depth, if yes change the flag to 1.
	flag = 0


	if (depth == LIMIT or flag == 1):
		return

	if (np.array_equal(board, solution)):
		print("\033[32m^Solution Found^\033[0m\n")
		FOUND = True

		print("\033[31m_Solution Steps_\033[0m")
		print("Step: %d" % depth)
		print(board)
		return


#Now you complete the recursive function to fill out to move your knights and check if the optimal solution is reached. If you do not check for optimality your code will be executing for hours without finding the solution.

    
    
    
    #Here you finish your coding
	if FOUND == True:
		print("Step: %d" % depth)
		print(board)
	
inFile = s.argv[1]
myList = fileAccess (inFile)


board[0] = myList[0]
board[1] = myList[1]
board[2] = myList[2]
board[3] = myList[3]
solution[0] = myList[5]
solution[1] = myList[6]
solution[2] = myList[7]
solution[3] = myList[8]
    
move(board, solution, 0)

