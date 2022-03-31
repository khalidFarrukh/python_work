from tkinter import *
from PIL import ImageTk, Image
import pyautogui
import cv2
import pickle
import socket
import numpy as np
import keyboard as kb
import mouse
import time
from threading import*
import multiprocessing
import os
import win32api
import time

def send_mouse_event():
    while True:
        left_click_event = win32api.GetKeyState(0x01)
        right_click_event = win32api.GetKeyState(0x02)
        middle_click_event = win32api.GetKeyState(0x04)
        if left_click_event<0:
            print("left pressed !")
        if right_click_event<0:
            print("right pressed !")
        if middle_click_event<0:
            print("middle pressed !")
        time.sleep(0.1)
send_mouse_event()