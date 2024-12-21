######## example.py ########
import csv as c
# We need CSV library to do delimiter parsing of the
# input file
from fpdf import FPDF
# We need fpdf library to manipulate a PDF file.

class circle:
	def __init__(self, shape):

# The constructor of the class circle. When a statement
# such as circle(param) is made, the constructor is
# called to allocate space for a circle object in
# memory then initialize it. In this example, it
# extracts each element of shape and assign it to the
# corresponding attribute.  For the circle class, the
# attributes are: type, x_coor, y_coor, radius, red,
# green, blue. It also has a method called draw. 

		self.type = shape[0] 
		self.x_coor = int(shape[1])
		self.y_coor = int(shape[2])
		self.radius = int(shape[3])
		self.red = int(shape[4])
		self.green = int(shape[5])
		self.blue = int(shape[6])
		print("done initializing\n")

	def draw(self):
# This method sets the cooresponding drawing parameters
# and then invoke the method. 

		callMethod = getattr(pdf, "ellipse")
# Note that we use reflection to check if a specific
# method is available in the pdf object. In this case,
# we check for ellipse. If it is available, the
# location of that method is returned, and then
# assigned to callMethod. If it is not available, an
# error is thrown.

		pdf.set_fill_color(self.red, self.green, self.blue)
# Set the fill color to the specified RGB values.

		callMethod(self.x_coor, self.y_coor, self.radius, self.radius,"FD")
# CallMethod refers to the location of ellipse method
# in pdf. Thus, the line above simply calls pdf.ellipse
# method, which draws a circle in this case.
class Rect:
	def __init__(self, shape):
		self.type = shape[0]
		self.x_coor = int(shape[1])
		self.y_coor = int(shape[2])
		self.width = int(shape[3])
		self.height = int(shape[4])
		self.red = int(shape[5])
		self.green = int(shape[6])
		self.blue = int(shape[7])
		print("done initializing\n")

	def draw(self):
		callAttrib = getattr(pdf, 'rect')
		pdf.set_fill_color(self.red, self.green, self.blue)
		callAttrib(self.x_coor, self.y_coor, self.width, self.height,"FD")

class Line:
	def __init__(self, shape):
		self.type = shape[0]
		self.x_coor1 = int(shape[1])
		self.y_coor1 = int(shape[2])
		self.x_coor2 = int(shape[3])
		self.y_coor2 = int(shape[4])
		self.line_width = int(shape[5])
		self.red = int(shape[6])
		self.green = int(shape[7])
		self.blue = int(shape[8])
		print("done initializing\n")
	def draw(self):
		callAttrib = getattr(pdf, 'line')
		pdf.set_line_width(self.line_width)
		pdf.set_draw_color(self.red, self.green, self.blue)
		callAttrib(self.x_coor1, self.y_coor1, self.x_coor2, self.y_coor2)
		pdf.set_draw_color(0,0,0)
		pdf.set_line_width(1.0)
class Ellipse:
	def __init__(self, shape):
		self.type = shape[0]
		self.x_coor = int(shape[1])
		self.y_coor = int(shape[2])
		self.width = int(shape[3])
		self.height = int(shape[4])
		self.red = int(shape[5])
		self.green = int(shape[6])
		self.blue = int(shape[7])
		print("done initializing\n")

	def draw(self):
		callAttrib = getattr(pdf, 'ellipse')
		pdf.set_fill_color(self.red, self.green, self.blue)
		callAttrib(self.x_coor, self.y_coor, self.width, self.height,"FD")



def fileAccess (filename):
# Method fileAccess that takes a filename as its only
# parameter.
	result =  []
# Declare a list called result and initialize it to an
# empty list.
	print('Opening file ', filename)

	with open(filename) as inFile: # create file object
# Open the input file as an object inFile
		print('Reading ', filename)

		for x in list(c.reader(inFile, delimiter= ',')):  
			# print (x, end = "\n")
			result.append(x)
# append each x to the result list. 
		print('Closing ', filename)

	inFile.close()  # close the file
# close the file.

	return result
# return the result list which is a two dimensional
# array.

######################################

# Main body of the program

pdf = FPDF()
# Instantiate an FPDF object called pdf.

pdf.add_page()
# Invoke method add_page in the pdf object.

pdf.set_line_width(1.0)
# Invoke method set_line_width in the pdf object.

pdf.set_draw_color(0)
# Invoke method set_draw_color in the pdf object.

myObj = [] 
# Declare a list, myObj and initialize it to an empty
# list.

inFile = input("Enter the input file name:")
# Ask the user to enter the input file. 

myList = fileAccess (inFile)
# All the content in the file is returned as a two
# dimensiional array. Each element contains each field
# in the file separated by commas.

for inf in myList:
# Extract each row (inf) from myList.
	if inf[0] == 'circle':
		myObj.append(circle(inf))
	elif inf[0] == 'rect':
		myObj.append(Rect(inf))
	elif inf[0] == 'line':
		myObj.append(Line(inf))
	elif inf[0] == 'ellipse':
		myObj.append(Ellipse(inf))
# Instantiate a circle object for each inf. Append each
# newly created object to an object list, myObj. 

for obj in myObj:
# Extract each object from myObj.
	obj.draw()
# Invoke the draw method to create a specific shape in
# memory.

pdf.output("C:/Users/simgo/PycharmProjects/CSCE 155A/projects/myOutput.pdf")
# Then output it to myCircles.pdf.
