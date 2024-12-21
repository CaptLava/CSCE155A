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


class Shapes:
    def __init__(self):
        self.stuck = False
        self.x1 = random.randint(0, frame_width - size)
        self.y1 = random.randint(0, frame_height - size)
        self.x2 = self.x1 + size
        self.y2 = self.y1 + size
        self.velx = 2
        self.vely = 2
        self.red = 123
        self.green = int((frame_height/2 - size/2) -175)
        self.blue = int((frame_width/2 - size/2) - 250)
        self.been_stuck = 0
        self.name = 'Other'
        self.shape_type = 'circle'

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
    def move_shapes(self):
        if not self.stuck:
            self.x1 += self.velx
            self.y1 += self.vely
            self.x2 = self.x1 + size
            self.y2 = self.y1 + size

class Circle(Shapes):

    def create_circles(self):
        canvas.create_oval([self.x1, self.y1, self.x2, self.y2],fill=dec2hex(self.red,self.green,self.blue), width=0)
        self.shape_type = 'circle'
    def first_circ(self):
        self.velx = 0
        self.vely = 0
        self.x1 = frame_width/2 - size/2
        self.y1 = frame_height/2 - size/2
        self.x2 = frame_width / 2 + size/2
        self.y2 = frame_height / 2 + size/2
        self.name = 'first'
        self.stuck = True
        self.shape_type = 'circle'

    def check_collision(self, other):
        if self.been_stuck < 1:
            if other.stuck or self.stuck:
                if other.shape_type == 'circle':
                    center_x1 = self.x1 + size/2
                    center_y1 = self.y1 + size / 2
                    center_x2 = other.x1 + size / 2
                    center_y2 = other.y1 + size / 2
                    distance = math.sqrt((center_x2 - center_x1)**2 + (center_y1 - center_y2)**2)
                    if distance<= size+1:
                        self.handle_collision()
                        return True
                elif other.shape_type == 'square':
                    if self.check_circle_square_collision(other):
                        self.handle_collision()
                        return True
                return False


    def handle_collision(self):
        self.velx = 0
        self.vely = 0
        self.stuck = True
        if self.name != 'first':
            if int(self.x1 - 250) >= 255:
                self.blue = int(self.x1 - 250) - 10
            elif int(self.x1 - 250) <= 0:
                self.blue = int(self.x1 - 250) + 10
            else:

                self.blue = int(self.x1 - 250)
            if int(self.y1 - 250) >= 255:
                self.green = int(self.y1 - 250) - 100
            elif int(self.y1 - 250) <= 0:
                self.green = int(self.y1 - 250) + 100
            else:

                self.green = int(self.y1 - 175)

        print(f'blue:{self.blue}; Green: {self.green} ; Red: {self.red}')
        self.been_stuck += 1
        return self.been_stuck


    def check_circle_square_collision(self, other):
        def point_in_circle(x,y):
            center_x = self.x1 + size / 2
            center_y = self.y1 + size / 2
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            if distance <= size /2:
                return True
            else:
                return False

        corners = [(other.x1, other.y1),(other.x1, other.y2),(other.x2, other.y1),(other.x2, other.y2)]

        for x in corners:
            if point_in_circle(x[0],x[1]):
                return True
        return False

class Square(Shapes):
    def create_squares(self):
        canvas.create_rectangle([self.x1, self.y1, self.x2, self.y2], fill=dec2hex(self.red,self.green,self.blue), width=0)
        self.shape_type = 'square'

    def check_collision(self, other):
        if other.shape_type =='square':
            if self.check_square_collision(other):
                self.handle_collision()
                return True
        elif other.shape_type == "circle":
            if other.check_circle_square_collision():
                self.handle_collision()
                return True
        return False

    def check_square_circle_collision(self, other):
        def point_in_square(x, y):
            if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
                return True
            return False
        corners = [(other.x1, other.y1), (other.x1, other.y2), (other.x2, other.y1), (other.x2, other.y2)]

        for x, y in corners:
            if point_in_square(x, y):
                return True
        return False

    def handle_collision(self):
        self.velx = 0
        self.vely = 0
        self.stuck = True
        if self.name != 'first':
            if int(self.x1 - 250) >= 255:
                self.blue = int(self.x1 - 250) - 10
            elif int(self.x1 - 250) <= 0:
                self.blue = int(self.x1 - 250) + 10
            else:

                self.blue = int(self.x1 - 250)
            if int(self.y1 - 250) >= 255:
                self.green = int(self.y1 - 250) - 100
            elif int(self.y1 - 250) <= 0:
                self.green = int(self.y1 - 250) + 100
            else:

                self.green = int(self.y1 - 175)

        print(f'blue:{self.blue}; Green: {self.green} ; Red: {self.red}')
        self.been_stuck += 1
        return self.been_stuck

    def check_square_collision(self, other):
        def is_inside(x,y,shape):
            if shape.x1 <= x <= shape.x2 and shape.y1 <= y <= shape.y2:
                return True
            else:
                return False


        corners_x = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y1), (self.x2, self.y2)]
        for x in corners_x:
            if is_inside(x[0], x[1], other):
                return True
        return False




def dec2hex(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

first_circle = Circle()
first_circle.first_circ()

shapes = [ Circle() for x in range(4)]
for i in range(len(shapes)):
    shapes[i].shape_type = 'circle'
squares = ([Square() for y in range(4)])
for i in range(len(squares)):
    shapes[i].shape_type = 'square'
shapes.extend(squares)


shapes.insert(0, first_circle)

all_stuck =0

while True:
    canvas.delete('all')
    canvas['bg'] = 'black'

    for y in range(0, frame_height, 100):
        canvas.create_rectangle([0,y, frame_width, y + 1], fill = 'Magenta', width = 0)

    for x in range(0,frame_width,100):
        canvas.create_rectangle([x,0,x+1,frame_height], fill = 'Magenta', width = 0)

    for i in range(len(shapes)):
        current = shapes[i]
        for j in range(i+1, len(shapes)):
            other_shape = shapes[j]
            if current.check_collision(other_shape) or other_shape.check_collision(current) == 1:
                all_stuck += 1
                print(all_stuck)
                if all_stuck %10 == 0:
                    new_circles = [Circle() for i in range(4)]
                    shapes.extend(new_circles)
                    new_squares =  [Square() for i in range(4)]
                    shapes.extend(new_squares)
                    if len(shapes) >30:
                        break

            #other_circle.change_color()
    first_circle.create_circles()
    for y in range(len(shapes)):
        shapes[y].move_shapes()
        if shapes[y].shape_type == 'square':
            shapes[y].create_squares()
        elif shapes[y].shape_type == 'circle':
            shapes[y].create_circles()
        else:
            shapes[y].create_squares()

        shapes[y].check_pos()



    canvas.update()
    time.sleep(.003)




root.destroy()




'''
                        if int(self.x1 -250) >= 255:
                            self.blue = int(self.x1 -250) - 5
                        elif int(self.x1 -250) <= 0:
                            self.blue = int(self.x1 -250)  +5
                        else:

                            self.blue = int(self.x1 -250)
                        if int(self.y1 -250) >= 255:
                            self.green = int(self.y1 -250) - 100
                        elif int(self.y1 -250) <= 0:
                            self.green = int(self.y1 -250)  +100
                        else:

                            self.green = int(self.y1 -175)
'''