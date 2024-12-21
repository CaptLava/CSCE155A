import tkinter as tk, time, random



root = tk.Tk()
w = 800
h = 600
g = print('%dx%d', (w,h))
root.geometry(g)
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width = w, height = h)
root.title('List of Things')
class Thing:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        s = random.randint(0,1)
        if s == 0:
            self.shape = 'square'
        elif s == 1:
            self.shape = 'circle'

    def move(self):
        self.position_x += random.randint(-5,5)
        self.position_y += random.randint(-5,5)

    def draw(self):
        x = self.position_x
        y = self.position_y
        if self.shape == 'square':
            canvas.create_rectangle([x,y, x+50, y+50], fill = 'green')
        elif self.shape == 'circle':
            canvas.create_oval([x,y,x+50,y+50], fill = 'purple')

list_of_things = []
for y in range(1,11):
    list_of_things.append(Thing(w/2,y*25))

while True:
    canvas.delete('all')
    for i in range(len(list_of_things)):
        list_of_things[i].move()
        list_of_things[i].draw()
    canvas.update()
    time.sleep(.01)
root.destroy()


