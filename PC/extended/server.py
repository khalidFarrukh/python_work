from ast import Name
import socket
import cv2
import numpy as np
import pyautogui
import keyboard as kb
import mouse
import time

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

hip = "192.168.0.105"
port = 1025
local_EP = (hip, port)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind(local_EP)
    s.listen(10)
    print("waiting for a connection 1....")
    clnt, c_address = s.accept()
    print(f"connection to {c_address} established")
    print("")

    msg = list(mouse.get_position())  # mouse location
    clnt.send(str(msg).encode("utf-8"))
    clnt.close()
    s.close()
    time.sleep(0.1)

# --------------------------------------------------------------------------
