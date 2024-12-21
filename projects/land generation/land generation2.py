import numpy as np, time, random

n = int(input('Input n value greater than 4: '))
seed = int(input('Input a value for the seed: '))
magnitude = int(input('Enter the offset: '))
random.seed(12)
depth = 0

length = (2**n)-1
array = np.full((length, length), '~', dtype=object)


def four_corners(): # initializes the original 4 corners
    global array
    array[0,0] = random.randint(0,99)
    array[0,length-1] = random.randint(0,99)
    array[length-1, 0] = random.randint(0,99)
    array[length-1,length-1] = random.randint(0,99)

def find_midpoint(x1,y1,x2,y2, depth): # x step, finds the middle value of the 4 corners
    global array

    middle_x = (x1+x2) // 2
    middle_y = (y1+y2) // 2




    midpoint_value = ((top_left + bottom_right + bottom_left + top_right) / 4) - magnitude
    array[middle_x, middle_y] = int(midpoint_value)


    if array[middle_x, middle_y] != '~':
        left_average = (top_right + top_left + midpoint_value) / 3
        right_average = (bottom_left + bottom_right + midpoint_value) / 3


        array[(x1 + x2) // 2, y1] = int(left_average + magnitude)  # left triangle
        array[(x1 + x2) // 2, y2] = int(right_average + magnitude)  # right triangle



    corners = [top_left, top_right, bottom_left, bottom_right]
    for i in corners:
        if i == '~':
            print('~ found on a corner')




    print('Depth:', depth)
    print_array()
    time.sleep(1)




    if x2 - x1 > 1:  # Continue subdividing if the quadrant can still be divided
        find_midpoint(x1, y1, middle_x, middle_y, depth + 1)  # Top-left quadrant
        find_midpoint(x1, middle_y, middle_x, y2, depth + 1)  # Top-right quadrant
        find_midpoint(middle_x, y1, x2, middle_y, depth + 1)  # Bottom-left quadrant
        find_midpoint(middle_x, middle_y, x2, y2, depth + 1)  # Bottom-right quadrant

    """
    top_left = array[0,0]
    top_right = array[0,length-1]
    bottom_left = array[length-1, 0]
    bottom_right = array[length-1,length-1]
    middle_point = ((top_left + bottom_right+bottom_left+top_right)/4)-magnitude
    mid_point_location = int(length/2)
    array[mid_point_location][mid_point_location] = middle_point

    """
def print_array():
    for x in range(len(array)):
        for y in range(len(array)):
            if y == len(array)-1:
                print(array[x, y])
            else:
                print(array[x,y], end = ' ')


def plus_step():
    global array




four_corners()
print_array()

time.sleep(2)

find_midpoint(0,0,length-1,length-1,depth)
print_array()