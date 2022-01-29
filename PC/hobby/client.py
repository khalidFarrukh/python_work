import socket
import keyboard

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
port = 1025
local_EP = (hip, port)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    try:
        while True:
            s.connect(local_EP)
            s.send(message.encode("utf-8"))
            print(msg)
        #     key = keyboard.read_key()
        #     a = 0
    except NameError:
        print(NameError)
        s.close()
except NameError:
    print("a")
    s.close()
