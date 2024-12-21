import numpy as np
import time
import os
depth = 0
shortest_path_so_far = 0

maze = np.full((12,12),'#')
maze[0] = ['#','#','#','#','#','#','#','#','#','#','#','#']
maze[1] = ['#',' ','#','#','#','#',' ','#',' ',' ',' ',' ']
maze[2] = ['#',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#']
maze[3] = ['#',' ','#','#','#','#',' ','#',' ','#',' ','#']
maze[4] = ['#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#']
maze[5] = ['#','#','#','#',' ','#',' ','#','#','#',' ','#']
maze[6] = ['#','#','#','#',' ','#',' ',' ','#',' ',' ','#']
maze[7] = ['#',' ',' ',' ',' ','#','#',' ','#',' ','#','#']
maze[8] = ['#',' ','#',' ','#','#','#',' ','#',' ','#','#']
maze[9] = ['#',' ','#',' ','#',' ','#',' ','#',' ','#','#']
maze[10] =['#',' ','#',' ',' ',' ',' ',' ','#',' ','#','#']
maze[11] =['#',' ','#','#','#','#','#','#','#','#','#','#']

def print_maze(arr, depth, path):
	print(f'Depth: {depth}, Shortest path found: {path}')
	for y in range(arr.shape[0]):
		for x in range(arr.shape[1]):
			if arr[y][x] == '#':
				print('\033[92m' + arr[y][x] + '\033[0m', end ='')
			else:
				print(arr[y][x], end ='')
		print()


def explore(maze, current_y, current_x, depth):
	global shortest_path_so_far
	maze[current_y][current_x] = '@'
	print_maze(maze, depth, shortest_path_so_far)

	if (current_y == 1 and current_x == 11): #The base case, we found the exit
		print("Found the exit!")

		time.sleep(1.5)
		shortest_path_so_far = depth

	time.sleep(0.25)
	print("\033[33A",end="\r")
	print("\n" * 5)

	maze_up = maze.copy()
	maze_down = maze.copy()
	maze_left = maze.copy()
	maze_right = maze.copy()    

	#################YOUR CODE STARTS HERE

	#Check up direction. If valid, recur up.
	if maze[current_y -1][current_x] == ' ':
		explore(maze_up,(current_y-1), current_x, depth+1)
	#Check left...
	if maze[current_y][current_x-1] == ' ':
		explore(maze_left,current_y, current_x-1, depth+1)
	#Check right...
	if current_x + 1 < len(maze):
		if maze[current_y][current_x+1] == ' ':
			explore(maze_right,current_y, current_x+1,depth+1)
	#Check down...
	if current_y + 1 < len(maze):
		if maze[current_y+1][current_x] == ' ':
			explore(maze_down,(current_y+1), current_x, depth+1)
	#################YOUR CODE ENDS HERE


	#If no direction to go next, start returning
	return  #Technically, once a function runs out of
		#instructions, it automatically 'returns' so this line is
		#just to show a point that we are returning.

print("\033[33A",end="\r")
explore(maze, 11, 1, depth) #Character starts at coordinate 11,1

