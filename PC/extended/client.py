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
    hip = "192.168.0.104"
    port = 1025
    local_s_ep = (hip, port)
    while True:
        local_cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cs.bind(local_s_ep)
        local_cs.listen(10)
        print("client to server : waiting for a connection")
        remote_sc, r_sc_address = local_cs.accept()
        print(f"connection to {r_sc_address} established")
        print("")
        img = pyautogui.screenshot()
        frame = np.array(img)
        remote_sc.send(pickle.dumps(frame))
        remote_sc.close()
        local_cs.close()


def get_mouse_position():
    rhip = "192.168.0.105"
    port = 1026
    remote_s_ep = (rhip, port)
    while True:
        local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cc.connect(remote_s_ep)
        temp = local_cc.recv(1024)
        m_pos = pickle.loads(temp)
        mouse.move(m_pos[0], m_pos[1])
        local_cc.close()


Thread(target=send_screen).start()
Thread(target=get_mouse_position).start()