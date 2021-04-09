from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image

from commands import get_watermark_img, get_image


root = Tk()
root.title("Watermarker")
file_names = []

get_watermark_button = ttk.Button(root, text="Get Watermark Image", command=get_watermark_img).grid(column=0,row=0)

get_image_button = ttk.Button(root, text="Get Image(s)", command=get_image).grid(column=1, row=0)

root.mainloop()