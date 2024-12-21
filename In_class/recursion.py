import time

def countdown(n):

    """
    while n >= 0:
        n-=1
        if (n==0):
            print('BLASTOFF')
            break
        else:
            print(str(n))
        time.sleep(.1)
    """
    if n<= 0:
        print('BLASTOFF')
        return
    print(n)
    time.sleep(.1)
    countdown(n-1)
    time.sleep(1)
    print('Going out %d' %n)

def line(k):
    if k <0:
        return
    for i in range(k):
        print('*', end = '')
    print()
    time.sleep(.1)
    line(k-1)
    for i in range(k):
        print('*', end ='')


#print('Going in %d')
#countdown(19)
#for i in range(20):
    #line(20 -i)
#for i in range(20):
    #line(i)
line(20)