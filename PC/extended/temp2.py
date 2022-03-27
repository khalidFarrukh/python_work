import pickle as pk
import cv2
import pyautogui
import numpy as np
import keyboard as kb
from PIL import ImageTk, Image
f1 = Image.Image.convert(pyautogui.screenshot(),'L')
print(len(f1))
cv2.imshow("frame image",f1)
if cv2.waitKey() & kb.is_pressed("esc"):
    cv2.destroyAllWindows()