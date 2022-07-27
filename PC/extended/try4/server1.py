from tkinter import *
from PIL import ImageTk
import pyautogui
import pickle
import socket

SCREEN_SIZE = tuple(pyautogui.size())

def get_screen():
    root = Tk()
    frame = pyautogui.screenshot()
    image2 = ImageTk.PhotoImage(frame)
    panel = Label(root,image=image2)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.attributes('-fullscreen', True)
    rhip = open("D:\server_client\_r_client_hip.txt","r").read() # direct internet ip
    port = 1025
    remote_s_ep = (rhip, port)
    while True: 
        local_sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
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
        local_sc.close()

if __name__ == "__main__":
    get_screen()