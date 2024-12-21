import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from enum import Enum
import sys


class Color(Enum):
    Red = 0
    Green = 1
    Blue = 2


def read_color(color_str):
    colors = {"r": Color.Red.value,
              "g": Color.Green.value,
              "b": Color.Blue.value}

    if (color_str not in colors):
        print("usage: denote color by first letter r, g, or b")
        sys.exit(2)
    return colors.get(color_str)


def image_decode(file_name, color, threshold):
    image_file = Image.open(file_name)
    image_data_old = np.asarray(image_file)
    image_data = image_data_old.copy()
    ################ YOUR CODE HERE
    for x in range(len(image_data)):
        for y in range(len(image_data)):
            if image_data[x][y][0] < image_data[x][y][1] and image_data[x][y][0] < image_data[x][y][2]:
                image_data[x][y] = (0,0,0)
            if image_data[x][y][1] < image_data[x][y][0] and image_data[x][y][1] < image_data[x][y][2]:
                image_data[x][y] = (255,255,255)
            if image_data[x][y][2] < image_data[x][y][0] and image_data[x][y][2] < image_data[x][y][1]:
                image_data[x][y] = (255,255,255)
    #image_data[0][0][2] = 255  # Example of editing blue value of first pixel

    ################
    processed_image = Image.fromarray(image_data)
    processed_image.save(f'decoded_{file_name}')
    render = ImageTk.PhotoImage(processed_image)
    return render


if (len(sys.argv) < 3):
    print("usage: %s [rgb] [threshold]" % sys.argv[0])
    sys.exit(1)


color = read_color(sys.argv[1].lower())
threshold = int(sys.argv[2])




File_Name = "21_Simon_Gomez.png"  # TODO: Change this filename to match yours
root = tk.Tk()
root.wm_title("Image Window")

processed_image = image_decode(File_Name, color, threshold)


