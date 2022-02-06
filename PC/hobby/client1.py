import socket
import keyboard
import time

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
hip = "192.168.0.105"
# hip = "10.0.2.15"
port = 1025
local_EP = (hip, port)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.connect(local_EP)
    msg = keyboard.read_key()
    s.send(str(msg).encode("utf-8"))
    print(msg)
    if msg == "esc":
        s.close()
        break
    time.sleep(0.1)
    s.close()
