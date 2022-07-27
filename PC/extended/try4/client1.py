import socket
from threading import *
import pickle
import pyautogui
from PIL import Image

SCREEN_SIZE = tuple(pyautogui.size())

def send_screen():
    hip = socket.gethostbyname(socket.gethostname()) # direct internet ip
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
        frame = Image.Image.convert(pyautogui.screenshot(),'L')
        remote_sc.send(pickle.dumps(frame))
        remote_sc.close()
        local_cs.close()


if __name__ == "__main__":
    send_screen()