import os
import tkinter as tk
from tkinter import filedialog

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.file_path = filedialog.askdirectory() + '/'
        self.main()

    
    def main(self):
        self.deleteFiles(self.readFolder())

    def readFolder(self):
        results = []
        for i in os.listdir(self.file_path):
            if 'sfk' in i.split('.')[-1]:
                results.append(i)
        return results

    def deleteFiles(self, files):
        for i in files:
            os.remove(self.file_path + i)

if __name__ == "__main__":
    window = Window()
    
