import numpy as np, time, random, os, sys

#n = int(input('Input n value greater than 4: '))
n = 5
#seed = int(input('Input a value for the seed: '))
seed = int(sys.argv[1])
y = int(sys.argv[2])

if y == 0:
    print('Cannot divide by zero, please rerun the program with a different magnitude')
    sys.exit()

random.seed(seed)

depth = 0

length = (2**n)+1


array = np.full((length, length), '~', dtype=object)

def four_corners(): # initializes the original 4 corners
    global array
    array[0,0] = random.randint(0,99)
    array[0,length-1] = random.randint(0,99)
    array[length-1, 0] = random.randint(0,99)
    array[length-1,length-1] = random.randint(0,99)

def calc_magnitude(depth):
    magnitude = random.randint(int(-16/((depth+1)*y)),int(16/((depth+1)*y)))
    return magnitude

def find_midpoint(x1,y1,x2,y2, depth): # implements the x step and plus step
    global array
    global magnitude
    magnitude = calc_magnitude(depth)
    if x2-x1 < 2 or y2 -y1 < 2: # returns once it cant go deeper
        return
    middle_x = (x1+x2) // 2
    middle_y = (y1+y2) // 2

    if array[x1, y1] != '~':
        top_left = array[x1, y1]
    else:
        top_left = 0
    if array[x1, y2] != '~':
        top_right = array[x1, y2]
    else:
        top_right = 0
    if array[x2, y1] != '~':
        bottom_left = array[x2, y1]
    else:
        bottom_left = 0
    if array[x2, y2] != '~':
        bottom_right = array[x2, y2]
    else:
        bottom_right = 0


    midpoint_value = ((top_left + bottom_right + bottom_left + top_right) / 4) - magnitude


    if array[middle_x, middle_y] == '~':
        array[middle_x, middle_y] = int(midpoint_value)
        print('Depth:', depth)
        print_array()
        time.sleep(.01)




    top_average = (top_right + top_left + midpoint_value) / 3
    bottom_average = (bottom_left + bottom_right + midpoint_value) / 3
    left_average = (top_left+ bottom_left+ midpoint_value)/3
    right_average = (top_right+bottom_right + midpoint_value) /3

    if array[x1, middle_y] == '~':
        array[x1, middle_y] = int( top_average+ magnitude) #top triangle
    if array[x2, middle_y] == '~':
        array[x2, middle_y] = int(bottom_average + magnitude)  #bottom triangle
    if array[middle_x, y1] == '~':
        array[middle_x, y1] = int(left_average+magnitude) #left triangle
    if array[middle_x, y2] == '~':
        array[middle_x, y2] = int(right_average + magnitude) #right triangle

    #do i need this?
    #corners = [top_left, top_right, bottom_left, bottom_right]
    #for i in corners:
    #    if i == '~':
    #        print('~ found on a corner')

    print('Depth:', depth)
    print_array()
    time.sleep(0.01)

    #changes where it is doing the algorithm on the array
    find_midpoint(x1, y1, middle_x, middle_y, depth + 1)  # Top-left
    find_midpoint(x1, middle_y, middle_x, y2, depth + 1)  # Top-right
    find_midpoint(middle_x, y1, x2, middle_y, depth + 1)  # Bottom-left
    find_midpoint(middle_x, middle_y, x2, y2, depth + 1)  # Bottom-right



def print_array():
    print('------------------------------------------------------------------------------------------------')
    for x in range(len(array)):
        for y in range(len(array)):
            val = array[x,y]
            if val!= '~':
                if val < 15:
                    val_color = '\033[44m'  #blue
                    val = '~'

                elif val < 40:
                    val_color = '\033[43m'  #yellow
                    val = '.'
                elif val < 65:
                    val_color = '\033[42m'  #green
                    val = '/'
                else:
                    val_color = '\033[47m'  #white
                    val = '^'
                reset = '\033[0m'
                print(f'{val_color}{val:>4}{reset}', end= '') #prints out symbol and backgroud color, then changes back to plain
            else:
                print(f'{val:>4}', end='')
        print()



four_corners()
print_array()
time.sleep(1)

find_midpoint(0,0,length-1,length-1,depth)


print_array()
print(length)

