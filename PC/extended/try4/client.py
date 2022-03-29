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
from pynput.mouse import Listener,Button,Controller
import os
os.system("cls")

SCREEN_SIZE = tuple(pyautogui.size())

# def send_screen():
#     hip = "192.168.0.107" # direct internet ip
#     #hip = "192.168.0.106" # wifi ip
#     port = 1025
#     local_s_ep = (hip, port)
#     while True:
#         local_cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
#         local_cs.bind(local_s_ep)
#         local_cs.listen(10)
#         print("\033[1;37;40m ")
#         print("client to server : waiting for a connection")
#         remote_sc, r_sc_address = local_cs.accept()
#         print(f"connection to {r_sc_address} established")
#         print("")
#         print("\033[1;37;40m ")
#         frame = Image.Image.convert(pyautogui.screenshot(),'L')
#         remote_sc.send(pickle.dumps(frame))
#         remote_sc.close()
#         local_cs.close()


# def get_mouse_position():
#     rhip = "192.168.0.105" # direct internet ip
#     port = 1026
#     remote_s_ep = (rhip, port)
#     while True:
#         local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
#         local_cc.connect(remote_s_ep)
#         temp = local_cc.recv(1024)
#         m_pos = pickle.loads(temp)
#         mouse.move(m_pos[0], m_pos[1])
#         local_cc.close()
mouse_rhip = "192.168.0.105" # direct internet ip
mouse_can_move_port = 1026
mouse_can_move_remote_s_ep = (mouse_rhip, mouse_can_move_port)
mouse_can_click_port = 1027
mouse_can_click_remote_s_ep = (mouse_rhip, mouse_can_click_port)
mouse_can_scroll_port = 1028
mouse_can_scroll_remote_s_ep = (mouse_rhip, mouse_can_scroll_port)


def mouse_can_move():
    mouse = Controller()
    while True:
        mouse_local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        mouse_local_cc.connect(mouse_can_move_remote_s_ep)
        temp = mouse_local_cc.recv(50)
        m_pos = pickle.loads(temp)
        mouse.position = (m_pos[0],m_pos[1])

        # if event == 'r':
        #     # mouse.click('right')
        #     print("                                  right")
        # elif event=='l':
        #     # mouse.click('left')
        #     print("left")
        # elif event == 'm':
        #     # mouse.click('middle')
        #     print("             middle")
        mouse_local_cc.close()

def mouse_can_click():
    mouse = Controller()
    while True:
        mouse_local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        mouse_local_cc.connect(mouse_can_click_remote_s_ep)
        temp = mouse_local_cc.recv(50)
        button_alias = pickle.loads(temp)
        
        if button_alias == "r":
            # mouse.click('right')
            print("                                  right")
        elif button_alias=="l":
            # mouse.click('left')
            print("left")
        elif button_alias == "m":
            # mouse.click('middle')
            print("             middle")
        mouse_local_cc.close()

def mouse_can_scroll():
    mouse = Controller()
    while True:
        mouse_local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        mouse_local_cc.connect(mouse_can_click_remote_s_ep)
        temp = mouse_local_cc.recv(50)
        scroll_values = pickle.loads(temp)
        mouse.scroll(scroll_values[0],scroll_values[1])
        mouse_local_cc.close()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    # p1 = multiprocessing.Process(target=send_screen,args=())
    p2 = multiprocessing.Process(target=mouse_can_move,args=())
    p3 = multiprocessing.Process(target=mouse_can_click,args=())
    p4 = multiprocessing.Process(target=mouse_can_scroll,args=())
    # p1.start()
    p2.start()
    p3.start()
    p4.start()
    # p1.join()
    p2.join()
    p3.join()
    p4.join()