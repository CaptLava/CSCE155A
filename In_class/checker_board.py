import tkinter as tk, time


frame_width = 800
frame_height = 300
root = tk.Tk()
root.geometry(f'{frame_width}x{frame_height}')
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width = frame_width, height = frame_height)
root.title('Checkerboard')





color = 'black'
size = 20
increment = 0

while True:
    canvas.delete('all')
    increment += 20
    if increment >= frame_width-(size*8):
        increment = 0
    for y in range(8):
        if color == 'black':
            color = 'white'
        elif color == 'white':
            color = 'black'
        for x in range(8):
            x1 = x*size + increment
            y1 = y*size + (frame_height - 8*size)/2
            x2 = x1+size
            y2 = y1+size
            canvas.create_rectangle([x1,y1,x2,y2], fill = color)

            if color == 'black':
                color = 'white'
            elif color == 'white':
                color = 'black'
            canvas.update()
        canvas.update()
    time.sleep(.1)


