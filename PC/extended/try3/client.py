import socket
import click
import keyboard as kb
import time
import subprocess
from threading import *
import mouse
import pickle
import pyautogui
import cv2
import numpy as np
from PIL import ImageTk, Image
import multiprocessing

SCREEN_SIZE = tuple(pyautogui.size())

def send_screen():
    hip = "192.168.0.107" # direct internet ip
    #hip = "192.168.0.106" # wifi ip
    port = 1025
    local_s_ep = (hip, port)
    while True:
        local_cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cs.bind(local_s_ep)
        local_cs.listen(10)
        print("\033[1;37;40m ")
        print("client to server : waiting for a connection")
        remote_sc, r_sc_address = local_cs.accept()
        print(f"connection to {r_sc_address} established")
        print("")
        print("\033[1;37;40m ")
        frame = Image.Image.convert(pyautogui.screenshot(),'L')
        remote_sc.send(pickle.dumps(frame))
        remote_sc.close()
        local_cs.close()


def get_mouse_position():
    rhip = "192.168.0.105" # direct internet ip
    port = 1026
    remote_s_ep = (rhip, port)
    while True:
        local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cc.connect(remote_s_ep)
        temp = local_cc.recv(1024)
        m_pos = pickle.loads(temp)
        mouse.move(m_pos[0], m_pos[1])
        local_cc.close()

def get_mouse_event():
    rhip = "192.168.0.105" # direct internet ip
    port = 1027
    remote_s_ep = (rhip, port)
    while True:
        local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cc.connect(remote_s_ep)
        temp = local_cc.recv(2)
        event = pickle.loads(temp)
        print("\033[1;36;40m hellow \n")
        print("                                                                event = ",event)
        print("\033[1;37;40m welcome \n")
        # if event == 'r':
        #     # mouse.click('right')
        #     print("                                  right")
        # elif event=='l':
        #     # mouse.click('left')
        #     print("left")
        # elif event == 'm':
        #     # mouse.click('middle')
        #     print("             middle")
        local_cc.close()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=send_screen,args=())
    p2 = multiprocessing.Process(target=get_mouse_position,args=())
    p3 = multiprocessing.Process(target=get_mouse_event,args=())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()