import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import rawpy
import imageio

class CR2toPNGConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CR2 to PNG Converter")
        self.create_gui()

    def create_gui(self):
        tk.Button(self.root, text="Select Folder", command=self.select_folder).pack(pady=20)
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(pady=10)
    
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.convert_folder(folder_path)
    
    def convert_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.lower().endswith('.cr2'):
                thread = threading.Thread(target=self.convert_file, args=(os.path.join(folder_path, filename),))
                thread.start()

    def convert_file(self, file_path):
        try:
            with rawpy.imread(file_path) as raw:
                rgb = raw.postprocess()
            imageio.imsave(f"{file_path[:-4]}.png", rgb)
            print(f"Converted {file_path} to PNG")
        except Exception as e:
            print(f"Failed to convert {file_path}: {str(e)}")

    def exit_app(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    converter = CR2toPNGConverter()
    converter.run()
