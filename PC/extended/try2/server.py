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
    rhip = "192.168.0.107" # direct internet ip
    #rhip = "192.168.0.106" # wifi ip
    port = 1025
    remote_s_ep = (rhip, port)
    while True:
        local_sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        try:
            local_sc.connect(remote_s_ep)
            temp = local_sc.recv(1024)
            rec_msg = pickle.loads(temp)
            print(rec_msg)
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
        print("waiting for a connection ....")
        remote_cs, r_cs_address = local_ss.accept()
        print(f"connection to {r_cs_address} established")
        print("")

        msg = "i am iron man"  # mouse location
        remote_cs.send(pickle.dumps(msg))
        remote_cs.close()
        local_ss.close()

p1 = multiprocessing.Process(target=send_mouse_position,args=())
p2 = multiprocessing.Process(target=get_screen,args=())
p1.start()
p2.start()
p1.join()
p2.join()
