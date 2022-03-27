from tkinter import *
from PIL import ImageTk, Image
import pyautogui
import cv2
import pickle as pk
root = Tk()
frame = pyautogui.screenshot()
image2 = ImageTk.PhotoImage(frame)
panel = Label(root,image=image2)
panel.pack(side="bottom", fill="both", expand="yes")
root.attributes('-fullscreen', True)
while True:
    #frame = pyautogui.screenshot()
    #d1 = pk.dumps(frame)
    #f1 = pk.loads(d1)
    #f1 = Image.frombytes()
    f1 = Image.Image.convert(pyautogui.screenshot(),'L')
    print(type(f1))
    image2 = ImageTk.PhotoImage(f1)
    panel.configure(image=image2)
    panel.image = image2
    root.attributes('-fullscreen', True)
    root.update()
#root.mainloop()