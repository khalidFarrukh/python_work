import socket

host = "192.168.0.105"
port = 1025
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
msg = ""
while True:
    temp = s.recv(8)
    if len(temp) == 0:
        break
    msg += temp.decode("utf-8")
print(msg)
