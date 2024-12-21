yard =['f','','h','','','','','','','']
count = 0


def chase(yard, depth):
    global count

    #finds hair with x
    for x in range(len(yard)):
        if yard[x] == 'h':
            break
    flag =0
    #finds fox with y
    for y in range(len(yard)):
        if yard[y] == 'f':
            flag = 1
            break


    #edge cases
        #if depth > 3:
        #return
    #when the fox win
    if flag == 0:
        print('Fox eats the hair')
        return



    #move the fox
    yard[y] = ''
    if x >y:
        yard[y+1] = 'f'
    if x < y:
        yard[y-1] = 'f'

    # increase count and print current state of the yard
    count+= 1
    print(count,depth,end = '')
    print(yard)

    # move hair and call function recursively

    yard_left = yard.copy()
    yard_right = yard.copy()

    #move hair left
    if x-2 >= 0:
        yard_left[x] = ''
        yard_left[x-2] = 'h'
        chase(yard_left, depth+1)
    #move hair right
    if x + 2 < len(yard):
        yard_right[x] = ''
        yard_right[x+2] = 'h'
        chase(yard_right, depth+1)

chase(yard,0)