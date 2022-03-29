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
            frame = pickle.loads(temp)
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
    hip = "192.168.0.105" # direct internet ip
    port = 1026
    local_s_ep = (hip, port)
    while True:
        local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_ss.bind(local_s_ep)
        local_ss.listen(10)
        print("\033[1;37;40m",end = "")
        print("waiting for a connection ....")
        remote_cs, r_cs_address = local_ss.accept()
        print(f"connection to {r_cs_address} established")
        print("")
        print("\033[1;37;40m",end = "")
        m_pos = list(mouse.get_position())  # mouse location
        remote_cs.send(pickle.dumps(m_pos))
        remote_cs.close()
        local_ss.close()

def send_mouse_event():
    hip = "192.168.0.105" # direct internet ip
    port = 1027
    local_s_ep = (hip, port)
    while True:
        local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_ss.bind(local_s_ep)
        local_ss.listen(10)
        print("\033[1;37;40m",end = "")
        print("waiting for a connection ....")
        remote_cs, r_cs_address = local_ss.accept()
        print(f"connection to {r_cs_address} established")
        print("")
        print("\033[1;37;40m",end = "")
        if mouse.is_pressed("right"):
            remote_cs.send(pickle.dumps("r"))
        elif mouse.is_pressed("left"):
            remote_cs.send(pickle.dumps("l"))
        elif mouse.is_pressed("middle"):
            remote_cs.send(pickle.dumps("m"))
        remote_cs.close()
        local_ss.close()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=send_mouse_position,args=())
    p2 = multiprocessing.Process(target=get_screen,args=())
    p3 = multiprocessing.Process(target=send_mouse_event,args=())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()