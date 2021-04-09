import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image


class Watermarker():
    def __init__(self, root):

        root.title("Watermarker")

        self.watermark = None
        self.file_names = []

        watermark_btn = ttk.Button(root, text="Select Watermark Image", command=self.get_watermark).grid(column=0,row=0)
        image_btn = ttk.Button(root, text="Get Image(s)", command=self.get_images).grid(column=1, row=0)

    def get_watermark(self):
        self.watermark = ImageTk.PhotoImage(Image.open(filedialog.askopenfilename(filetypes=[('images', '*.jpg *.jpeg *.png')])))
        watermark_label = ttk.Label(image=self.watermark)
        watermark_label.grid(column=0, row=1)

    def get_images(self):
        image_paths = filedialog.askopenfilenames(filetypes=[('images', '*.jpg *.jpeg *.png')])
        for path in image_paths:
            file_name = os.path.basename(path)
            self.file_names.append(file_name)

        print(self.file_names)


root = Tk()
Watermarker(root)
root.mainloop()