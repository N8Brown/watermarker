import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image


def get_watermark_img():
    global watermark_img
    watermark_img = ImageTk.PhotoImage(Image.open(filedialog.askopenfilename(filetypes=[('images', '*.jpg *.jpeg *.png')])))
    watermark_label = ttk.Label(image=watermark_img)
    watermark_label.grid(column=0, row=1)


def get_image():
    global file_names
    image_paths = filedialog.askopenfilenames(filetypes=[('images', '*.jpg *.jpeg *.png')])
    # file_names = [os.path.basename(path) for path in image_paths]

    for path in image_paths:
        file_name = os.path.basename(path)
        file_names.append(file_name)

    print(file_names)
