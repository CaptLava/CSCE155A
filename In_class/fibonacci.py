import tkinter as tk, time

frame_height = 500
frame_width = 500
root = tk.Tk()
root.geometry(f'{frame_width}x{frame_height}')
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width = frame_width, height = frame_height)
root.title('fibonacci')


color = 'red'



num1 = 0
num2 = 1
length = int(input('How far would you like the sequence to calculate to?'))

def fib(num1,num2, length):
    start_length = 2
    for i in range(length):

        tmp =num1+num2
        print(f'{num1} + {num2} = {tmp}')

        x1 = num1 + 250
        y1 = num2 + 250
        num1 = num2
        num2 = tmp
        x2 = num1 +250
        y2 = num2 + 250

        canvas.create_line([x1,y1, x2,y2], fill=color, width=2, smooth=1)
        canvas.update()
        time.sleep(.5)





canvas.update()

fib(num1,num2, length)


#Fibonacci using recursive:
