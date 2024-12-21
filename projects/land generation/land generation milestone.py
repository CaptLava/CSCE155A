import numpy as np
import random

# Parameters for a 9x9 grid
n = 4  # Size of the array (for a 9x9 array)
magnitude = random.randint(-3, 3)  # Random offset between -3 and 3
length = (2**(n)) + 1  # Formula for calculating size (this results in a 9x9 array)
array = np.full((length, length), '~', dtype=object)  # Initialize array with '~'

# Initialize corners
array[0, 0] = 48  # Top left corner value
array[0, length-1] = 1  # Top right corner value
array[length-1, 0] = 21  # Bottom left corner value
array[length-1, length-1] = 12  # Bottom right corner value

def print_array():
    for x in range(len(array)):
        for y in range(len(array)):
            if y == len(array)-1:
                print(array[x, y])
            else:
                print(array[x, y], end=' ')

def find_midpoint(x1, y1, x2, y2, depth):
    global array

    if x2 - x1 < 2 or y2 - y1 < 2:  # Base case: if the quadrant cannot be subdivided
        return

    # Calculate midpoint coordinates
    middle_x = (x1 + x2) // 2
    middle_y = (y1 + y2) // 2

    # Get the corner values and handle any '~' values
    top_left = array[x1, y1] if array[x1, y1] != '~' else 0
    top_right = array[x1, y2] if array[x1, y2] != '~' else 0
    bottom_left = array[x2, y1] if array[x2, y1] != '~' else 0
    bottom_right = array[x2, y2] if array[x2, y2] != '~' else 0

    # Calculate midpoint value (center of four corners)
    midpoint_value = ((top_left + top_right + bottom_left + bottom_right) / 4) - magnitude
    if array[middle_x, middle_y] == '~':
        array[middle_x, middle_y] = int(midpoint_value)

    # Calculate top, bottom, left, and right averages (handle '~' if necessary)
    top_average = (top_left + top_right + midpoint_value) / 3
    bottom_average = (bottom_left + bottom_right + midpoint_value) / 3
    left_average = (top_left + bottom_left + midpoint_value) / 3
    right_average = (top_right + bottom_right + midpoint_value) / 3

    # Set the top, bottom, left, and right midpoints if not already set
    if array[x1, middle_y] == '~':  # Top edge
        array[x1, middle_y] = int(top_average + magnitude)

    if array[x2, middle_y] == '~':  # Bottom edge
        array[x2, middle_y] = int(bottom_average + magnitude)

    if array[middle_x, y1] == '~':  # Left edge
        array[middle_x, y1] = int(left_average + magnitude)

    if array[middle_x, y2] == '~':  # Right edge
        array[middle_x, y2] = int(right_average + magnitude)
    print_array()

    # Recursively divide into 4 smaller quadrants
    find_midpoint(x1, y1, middle_x, middle_y, depth + 1)  # Top-left quadrant
    find_midpoint(x1, middle_y, middle_x, y2, depth + 1)  # Top-right quadrant
    find_midpoint(middle_x, y1, x2, middle_y, depth + 1)  # Bottom-left quadrant
    find_midpoint(middle_x, middle_y, x2, y2, depth + 1)  # Bottom-right quadrant

# Start the midpoint finding and recursive filling
find_midpoint(0, 0, length - 1, length - 1, 0)

# Print the final array
print('---------------------------------------------------------')
print_array()