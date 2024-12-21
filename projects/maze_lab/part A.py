import numpy as np
import time
import os

maze = np.full((10,10),'#')
maze[0] = ['#','#','#','#','#','#','#','#','#','#']
maze[1] = ['#',' ',' ',' ','#',' ','#',' ',' ','#']
maze[2] = ['#',' ','#',' ','#',' ','#',' ','#','#']
maze[3] = ['#',' ','#',' ',' ',' ',' ',' ',' ','#']
maze[4] = ['#','#','#','#','#',' ','#','#',' ','#']
maze[5] = ['#',' ',' ',' ','#',' ',' ','#',' ','#']
maze[6] = ['#',' ','#',' ','#',' ','#',' ',' ','#']
maze[7] = ['#',' ','#',' ','#',' ','#',' ','#','#']
maze[8] = ['#',' ','#',' ',' ',' ','#',' ',' ',' ']
maze[9] = ['#','#','#',' ','#','#','#','#','#','#']

def print_maze(arr):
	for y in range(arr.shape[0]):
		for x in range(arr.shape[1]):
			if arr[y][x] == '#':
				print('\033[92m' + arr[y][x] + '\033[0m', end ='')
			else:
				print(arr[y][x], end ='')
		print()


def explore(maze, current_y, current_x):

	maze[current_y][current_x] = '@'
	print_maze(maze)

	if (current_y == 8 and current_x == 9): #The base case, we found the exit
		print("Found the exit!")
		time.sleep(3)
		exit()

	time.sleep(0.5)
	os.system("cls||clear")

	maze_up = maze.copy()
	maze_down = maze.copy()
	maze_left = maze.copy()
	maze_right = maze.copy()

	#################YOUR CODE STARTS HERE

	#Check up direction. If valid, recur up.
	if maze[current_y -1][current_x] == ' ':
		explore(maze_up,(current_y-1), current_x)
	#Check left...
	if maze[current_y][current_x-1] == ' ':
		explore(maze_left,current_y, current_x-1)
	#Check right...
	if maze[current_y][current_x+1] == ' ':
		explore(maze_right,current_y, current_x+1)
	#Check down...
	if current_y + 1 < len(maze):
		if maze[current_y+1][current_x] == ' ':
			explore(maze_down,(current_y+1), current_x)
	#################YOUR CODE ENDS HERE


	#If no direction to go next, start returning
	return  #Technically, once a function runs out of
		#instructions, it automatically 'returns' so this line is
		#just to show a point that we are returning.

os.system("cls||clear")
explore(maze, 9, 3) #Character starts at coordinate 3,9

