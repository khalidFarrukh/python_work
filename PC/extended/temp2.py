from tkinter import *
import time
class App:
    def __init__(self, master):
        self.slogan = Button(command=self.change)
        self.slogan.pack()
        self.title('abc')
        self.geometry('300x200')
        self.config(bg='#4a7a8c')
    def change(self):
        self.slogan.configure(bg='red')
        self.slogan.after(1000, self.change_back)

    def change_back(self):
        self.slogan.configure(bg='blue')

root = Tk()
app = App(root)
root.mainloop()