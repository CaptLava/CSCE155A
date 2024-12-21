import tkinter as tk, time, random, math
root = tk.Tk()
frame_width = 700
frame_height = 500

g = print('dx%d', (frame_width, frame_height))

root.geometry(g)
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width = frame_width, height = frame_height)
root.title()

size = 20
x1 = frame_width/2
y1 = frame_height/4


class Circles:
    def __init__(self):
        self.stuck = False
        self.x1 = random.randint(0, frame_width - size)
        self.y1 = random.randint(0, frame_height - size)
        self.x2 = self.x1 + size
        self.y2 = self.y1 + size
        self.velx = 1.0
        self.vely = 1.0
        self.red = 123
        self.green = int((frame_height/2 - size/2) -175)
        self.blue = int((frame_width/2 - size/2) - 250)
        self.been_stuck = 0
        self.name = 'Other'

    def change_vel(self):

        if self.x1 < 0 or self.x2 > frame_width:
            self.velx = -self.velx
        if self.y2 > frame_height or self.y1 < 0:
            self.vely = -self.vely
    def check_pos(self):
        if self.x1 < 0 or self.x2 > frame_width:
            self.change_vel()
        if self.y2 > frame_height or self.y1 < 0:
            self.change_vel()
    def move_circles(self):
        if not self.stuck:
            self.x1 += self.velx
            self.y1 += self.vely
            self.x2 = self.x1 + size
            self.y2 = self.y1 + size


    def create_circles(self):
        canvas.create_oval([self.x1, self.y1, self.x2, self.y2],fill=dec2hex(self.red,self.green,self.blue), width=0)

    def first_circ(self):
        self.velx = 0
        self.vely = 0
        self.x1 = frame_width/2 - size/2
        self.y1 = frame_height/2 - size/2
        self.x2 = frame_width / 2 + size/2
        self.y2 = frame_height / 2 + size/2
        self.name = 'first'
        self.stuck = True

    def check_collision(self, other):
        if self.been_stuck < 1:
            if other.stuck or self.stuck:
                center_x1 = self.x1 + size/2
                center_y1 = self.y1 + size / 2
                center_x2 = other.x1 + size / 2
                center_y2 = other.y1 + size / 2
                distance = math.sqrt((center_x2 - center_x1)**2 + (center_y1 - center_y2)**2)
                if distance<= size+2:
                    self.velx = 0
                    self.vely = 0
                    self.stuck = True
                    if self.name != 'first':
                        new_blue = int(self.x1 - 250)
                        if new_blue >= 255:
                            self.blue = new_blue - 5
                        elif new_blue <= 0:
                            self.blue = new_blue + 5
                        else:
                            self.blue = new_blue

                        new_green = int(self.y1 - 250)
                        if new_green >= 255:
                            self.green = new_green - 100
                        elif new_green <= 0:
                            self.green = new_green + 100
                        else:
                            self.green = new_green - 175

                        self.blue = max(0, min(255, self.blue))
                        self.green = max(0, min(255, self.green))

                    self.been_stuck +=1
                    return self.been_stuck

    def check_stuck(self):
        return self.stuck







def dec2hex(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

first_circle = Circles()

circles = [Circles() for x in range(9)]
first_circle.first_circ()

circles.insert(0, first_circle)
all_stuck =0

while True:
    canvas.delete('all')
    canvas['bg'] = 'black'

    for y in range(0, frame_height, 100):
        canvas.create_rectangle([0,y, frame_width, y + 1], fill = 'Magenta', width = 0)

    for x in range(0,frame_width,100):
        canvas.create_rectangle([x,0,x+1,frame_height], fill = 'Magenta', width = 0)

    for i in range(len(circles) +1):

        current = circles[i-1]
        for j in range(i+1, len(circles)):
            other_circle = circles[j]
            if current.check_collision(other_circle) or other_circle.check_collision(current) == 1:
                all_stuck += 1
                print(all_stuck)
                if all_stuck %10 == 0:

                    new_circles = [Circles() for i in range(10)]
                    for i in range(len(new_circles)):
                        circles.append(new_circles[i])
                        if len(circles) >50:
                            break

            #other_circle.change_color()
    for x in circles:
        x.move_circles()
        x.create_circles()
        x.check_pos()

    first_circle.create_circles()

    canvas.update()
    time.sleep(.001)



root.destroy()