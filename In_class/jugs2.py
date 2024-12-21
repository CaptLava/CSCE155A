import time

from test.test_importlib.util import case_insensitive_tests


def display_jugs(arr):
    print('J8:', 'O'*arr[0])
    print('J5: ', 'O'*arr[1])
    print('J3:' 'O'*arr[2])

Best = 999
def jugSolver(j6, j5, j3, depth):
    global Best
    print('Depth: %d' % depth)
    print('Best: %d' % Best)
    display_jugs([j6, j5, j3])
    print('-----------------')


    #Base case
    if j6 ==4 or j5 ==4:
        print('Solution Found!')
        if depth<Best:
            Best = depth
        time.sleep(.5)
        return

    #no need waste time exploring paths
    if depth == Best or depth>9:
        return

    #moves for the water

    if j6 > 0:
        if j5<5:
            x = 5-j5 # amount j5 can be given
            y = max(0,j6-x) #dont let j8 be negative
            z = j6-y # amount j8 can be given to j5
            jugSolver(y, j5+z, j3, depth+1)


        if j3 <3:
            x = 3-j3  # empty space in j3
            y = max(0, j6-x) # new amount in j8 after giving to j3
            z = j6-y #amount j8 is giving j3
            jugSolver(y, j5, j3+z, depth+1)

    if j5>0:
        if j6<6:
            x = 6-j6
            y = max(0, j5-x)
            z = j5 - y
            jugSolver(j6+z, y, j3, depth+1)

        if j3<3:
            x = 3-j3
            y = max(0, j5-x)
            z = j5-y
            jugSolver(j6, y, j3+z, depth+1)

    if j3>0:
        if j6<6:
            x = 6 - j6
            y = max(0, j3 - x)
            z = j3 - y
            jugSolver(j6+z, j5, y, depth + 1)

        if j5<5:
            x = 5-j5
            y = max(0, j3-x)
            z = j3-z
            jugSolver(j6, j5+z, y, depth+1)

jugSolver(6,0,0,0)
print('Fastest Solutoin requires %d moves' % Best)


