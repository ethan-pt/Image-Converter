import tkinter as tk
from tkinter import filedialog
from PIL import Image

# initialize window
root = tk.Tk()

# window settings
root.title("Image Converter")
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(3, weight=2)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(4, weight=2)

# button logic
def get_img():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    #im1 = Image.open(import_file_path)

def conv_jpg():
    rgb_im1 = im1.convert('RGB')
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    rgb_im1.save(export_file_path)

def conv_png():
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

# define/display label
label_1 = tk.Label(root, text="Image Converter", )
label_1.grid(row=0, column=1, columnspan=2, pady=10)

# define/display buttons
button_browse = tk.Button(root, text="Browse", command=get_img)
button_2 = tk.Button(root, text="Convert to PNG", command=conv_png)
button_3 = tk.Button(root, text="Convert to JPG", command=conv_jpg)

button_browse.grid(row=2, column=1, columnspan=2, pady=20)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)


# window loop
root.mainloop()