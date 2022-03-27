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
from threading import *

SCREEN_SIZE = tuple(pyautogui.size())
def get_screen():
    root = Tk()
    frame = pyautogui.screenshot()
    image2 = ImageTk.PhotoImage(frame)
    panel = Label(root,image=image2)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.attributes('-fullscreen', True)
    rhip = "192.168.0.107" # direct internet ip
    #rhip = "192.168.0.106" # wifi ip
    port = 1025
    remote_s_ep = (rhip, port)
    while True:
        local_sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        try:
            local_sc.connect(remote_s_ep)
            temp = b""
            while True:
                packet = local_sc.recv(1048576)
                if not packet:
                    break
                temp += packet
            #frame = pickle.loads(temp)
            #frame = pyautogui.screenshot()
            #d1 = pk.dumps(frame)
            #f1 = pk.loads(d1)
            frame = Image.frombytes(temp)
            image2 = ImageTk.PhotoImage(frame)
            panel.configure(image=image2)
            panel.image = image2
            root.attributes('-fullscreen', True)
            root.update()
            if kb.is_pressed("esc"):
                break
            local_sc.close()
        except NameError as e:
            print(e)
            local_sc.close()
            return -1

def send_mouse_position():
    hip = "192.168.0.105"
    port = 1026
    local_s_ep = (hip, port)
    while True:
        local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_ss.bind(local_s_ep)
        local_ss.listen(10)
        print("waiting for a connection 1....")
        remote_cs, r_cs_address = local_ss.accept()
        print(f"connection to {r_cs_address} established")
        print("")

        m_pos = list(mouse.get_position())  # mouse location
        remote_cs.send(pickle.dumps(m_pos))
        remote_cs.close()
        local_ss.close()

t1 = Thread(target=get_screen)
t2 = Thread(target=send_mouse_position)
t1.start()
t2.start()
t1.join()
t2.join()
