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
from pynput.mouse import Listener,mouse,Controller
import os
os.system("cls")

mouse_hip = "192.168.0.105" # direct internet ip
mouse_port = 1026
mouse_local_s_ep = (mouse_hip, mouse_port)

def on_move(x, y):
    mouse_local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    mouse_local_ss.bind(mouse_local_s_ep)
    mouse_local_ss.listen(10)
    print("\033[1;37;40m")
    print("waiting for a connection ....")
    mouse_remote_cs, m_r_cs_address = mouse_local_ss.accept()
    print(f"connection to {m_r_cs_address} established")
    print("")
    print("\033[1;37;40m")
    m_pos = list(x,y)  # mouse location
    mouse_remote_cs.send(pickle.dumps(m_pos))
    mouse_remote_cs.close()
    mouse_local_ss.close()
    

def on_click(x, y, button, pressed):
    mouse_local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    mouse_local_ss.bind(mouse_local_s_ep)
    mouse_local_ss.listen(10)
    print("\033[1;37;40m")
    print("waiting for a connection ....")
    mouse_remote_cs, m_r_cs_address = mouse_local_ss.accept()
    print(f"connection to {m_r_cs_address} established")
    print("")
    print("\033[1;37;40m")
    if pressed:
        if button.name == "left":
            # print("left button")
            mouse_remote_cs.send(pickle.dumps("l"))
        elif button.name == "right":
            # print("right button")
            mouse_remote_cs.send(pickle.dumps("r"))
        elif button.name == "middle":
            # print("middle button")
            mouse_remote_cs.send(pickle.dumps("m"))
    mouse_remote_cs.close()
    mouse_local_ss.close()

def on_scroll(x, y, dx, dy):
    mouse_local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    mouse_local_ss.bind(mouse_local_s_ep)
    mouse_local_ss.listen(10)
    print("\033[1;37;40m")
    print("waiting for a connection ....")
    mouse_remote_cs, m_r_cs_address = mouse_local_ss.accept()
    print(f"connection to {m_r_cs_address} established")
    print("")
    print("\033[1;37;40m")
    print(x, y, dx, dy)
    m_pos_scroll = list(x,y,dx,dy)  # mouse location
    mouse_remote_cs.send(pickle.dumps(m_pos_scroll))
    mouse_remote_cs.close()
    mouse_local_ss.close()

def send_mouse_event():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=send_mouse_event,args=())
    p1.start()
    p1.join()