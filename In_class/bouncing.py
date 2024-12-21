import tkinter as tk, time
root = tk.Tk()
frame_width = 800
frame_height = 600

g = print('dx%d', (frame_width, frame_height))

root.geometry(g)
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width = frame_width, height = frame_height)
root.title()

size = 50
x1 = frame_width/2
y1 = frame_height/4

velx = 2
vely = 2






while True:
    canvas.delete('all')
    canvas['bg'] = 'gray'

    x1 += velx
    y1 += vely
    x2 = x1+size
    y2 = y1+size

    if x1 < 0 or x2 > frame_width:
        velx = -velx
    if y2 > frame_height or y1 < 0:
        vely = -vely

    for y in range(0, frame_height, 40):
        canvas.create_rectangle([0,y, frame_width, y + 1], fill = 'Magenta', width = 0)

    for x in range(0,frame_width,40):
        canvas.create_rectangle([x,0,x+1,frame_height], fill = 'Magenta', width = 0)

    canvas.create_oval([x1,y1,x2,y2], fill = 'Red', width = 0)

    vely += .2


    canvas.update()


    time.sleep(.005)


root.destroy()