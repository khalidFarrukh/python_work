import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1024
s.connect((host, port))
msg = ""
while True:
    T = s.recv(8)
    if len(T) == 0:
        break
    msg += T.decode("utf-8")
print(msg)
