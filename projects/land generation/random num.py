'''
import random

while True:
    type1 = input('Square or Triangle(s or t):')
    if type1 == 's':

        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        num4 = int(input())
        total = ((num1+num2+num3+num4)/4) + random.randint(-3,3)
        print(total)
    elif type1 == 't':
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        total = ((num1 + num2 + num3) / 3) + (random.randint(-3, 3))
        print(total)
'''
class Shape:
    def __init__(x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

w = 10
h = 20
s1 = Shape(0, 0, w, h, 'Red')
