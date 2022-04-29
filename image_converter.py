from PIL import Image
from tkinter import *


# initialize window
root = Tk()

# window settings
root.title("Image Converter")
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(3, weight=2)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(4, weight=2)

# button logic

# define/display label
label_1 = Label(root, text="Image Converter", )
label_1.grid(row=0, column=1, columnspan=2, pady=10)

# define/display buttons
button_browse = Button(root, text="Browse", )
button_2 = Button(root, text="JPG to PNG", )
button_3 = Button(root, text="PNG to JPG", )

button_browse.grid(row=2, column=1, columnspan=2, pady=20)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)


# window loop
root.mainloop()