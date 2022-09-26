import tkinter as tk
from tkinter import filedialog
from PIL import Image


class App:
    def __init__(self, root):
        self.root = root

        # Tells window how to handle being resized
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(3, weight=2)
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(4, weight=2)

        # Define stuff
        self.label_1 = tk.Label(root, text="Image Converter", )
        self.button_browse = tk.Button(root, text="Browse", command=self.get_img)
        self.button_2 = tk.Button(root, text="Convert to PNG", command=self.conv_png)
        self.button_3 = tk.Button(root, text="Convert to JPG", command=self.conv_jpg)

        # Display stuff
        self.label_1.grid(row=0, column=1, columnspan=2, pady=10)
        self.button_browse.grid(row=2, column=1, columnspan=2, pady=20)
        self.button_2.grid(row=3, column=1, padx=5, pady=5)
        self.button_3.grid(row=3, column=2, padx=5, pady=5)

    # button logic
    def get_img(self):
        global im1
        import_file_path = filedialog.askopenfilename()
        im1 = Image.open(import_file_path)

    def conv_jpg(self):
        rgb_im1 = im1.convert('RGB')
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
        rgb_im1.save(export_file_path)

    def conv_png(self):
        export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
        im1.save(export_file_path)


def main():
    root = tk.Tk()
    root.title('Image Converter')

    window = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()