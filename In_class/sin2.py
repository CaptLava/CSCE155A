import time, math, random
import tkinter as tk



root = tk.Tk()

Frame_Width = 400
Frame_Height = 400
root.geometry('%dx%d'  % (Frame_Width, Frame_Height))
canvas = tk .Canvas(root)
canvas.pack()
canvas.config(width = Frame_Width, height = Frame_Height)
root.title('Rotate')

size = 50

for i in range(1, 1000):
    temp = random.randint(0,10)
    if temp <5:
        color = 'blue'
    elif temp > 5:
        color = 'green'
    elif temp == 5:
        color = 'red'
    px = Frame_Width/2 - 25
    py = Frame_Height/12 - 25
    a = i/3 * math.cos(i/15) +px
    b = i / 3 *math.sin(i/15) + py
    canvas.create_oval([a,b,a+size, b+size], fill = color)
    canvas.update()
    time.sleep(.01)
root.destroy()

