from tkinter import *
from PIL import ImageTk, Image
import pyautogui
import cv2
root = Tk()
frame = pyautogui.screenshot()
image2 = ImageTk.PhotoImage(frame)
panel = Label(root,image=image2)
panel.pack(side="bottom", fill="both", expand="yes")
root.attributes('-fullscreen', True)
while True:
    frame = pyautogui.screenshot()
    image2 = ImageTk.PhotoImage(frame)
    panel.configure(image=image2)
    panel.image = image2
    root.attributes('-fullscreen', True)
    root.update()
root.mainloop() 