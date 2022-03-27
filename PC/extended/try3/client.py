import socket
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

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_name = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print(host_name, " ", host_ip)
# port = 1025
# s.connect((host_ip, port))
# msg = ""
# while True:
#     temp = s.recv(8)
#     if len(temp) == 0:
#         break
#     msg += temp.decode("utf-8")
# print(msg)
# s.close()

# --------------------------------------------------------------

# hip = "192.168.0.105"
# port = 1025
# local_EP = (hip, port)
# while True:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
#     s.connect(local_EP)
#     msg = list(mouse.get_position())  # mouse location
#     s.send(str(msg).encode("utf-8"))
#     print(msg)
#     if msg == "esc":
#         s.close()
#         break
#     s.close()
#     time.sleep(0.1)

# --------------------------------------------------------------

SCREEN_SIZE = tuple(pyautogui.size())
g_m_p_check = False
s_s_f_check = False


def send_screen():
    hip = "192.168.0.107" # direct internet ip
    #hip = "192.168.0.106" # wifi ip
    port = 1025
    local_s_ep = (hip, port)
    while True:
        local_cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cs.bind(local_s_ep)
        local_cs.listen(10)
        print("client to server : waiting for a connection")
        remote_sc, r_sc_address = local_cs.accept()
        print(f"connection to {r_sc_address} established")
        
        msg = "i am super man"  # mouse location 
        remote_sc.send(pickle.dumps(msg))
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
        rec_msg = pickle.loads(temp)
        print(rec_msg)
        local_cc.close()


if __name__ == "__main__":
    #multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=send_screen,args=())
    p2 = multiprocessing.Process(target=get_mouse_position,args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()