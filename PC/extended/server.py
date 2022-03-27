from ast import Name
from concurrent.futures import thread
import socket
import cv2
import numpy as np
import pyautogui
import keyboard as kb
import mouse
import time
import pickle
from threading import *

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_name = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print(host_name, " ", host_ip)
# port = 1025
# s.bind((host_ip, port))
# while True:
#     s.listen(15)
#     client, caddress = s.accept()
#     print(f"connection to {caddress} established")
#     message = "Socket programming in python"
#     client.send(message.encode("utf-8"))
#     if client.close():
#         break
# s.close()

# --------------------------------------------------------------

# hip = "192.168.0.105"
# port = 1025
# local_EP = (hip, port)
# while True:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
#     s.bind(local_EP)
#     s.listen(10)
#     print("waiting for a connection....")
#     clnt, c_address = s.accept()
#     print(f"connection to {c_address} established")
#     print("")
#     msg = clnt.recv(1024).decode("utf-8")
#     print(type(msg))
#     msg = eval(msg)
#     print(type(msg))
#     clnt.close()
#     if msg == "esc":
#         print("client closed by user")
#     else:
#         print(msg)
#     s.close()
# --------------------------------------------------------------
SCREEN_SIZE = tuple(pyautogui.size())
global thread1_faliure
global thread2_faliure


# servers --- > client
def get_screen():
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
            window_name = "live screen"
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_name, SCREEN_SIZE[0] - 1, SCREEN_SIZE[1] - 1)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(window_name, frame)
            if cv2.waitKey() & kb.is_pressed("esc"):
                break
            cv2.destroyAllWindows()
            local_sc.close()
        except NameError as e:
            print(e)
            local_sc.close()
            return -1

    cv2.destroyAllWindows()


# servers --- > server
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


# --------------------------------------------------------------------------
