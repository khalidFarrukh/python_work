import pyautogui
import pickle
import numpy as np
import keyboard as kb
import cv2

SCREEN_SIZE = tuple(pyautogui.size())
while(True):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    window_name = 'live screen'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, SCREEN_SIZE[0] - 1, SCREEN_SIZE[1] - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, frame)
    if kb.is_pressed('esc'):
        cv2.destroyAllWindows()
        break
    cv2.destroyAllWindows()
    
