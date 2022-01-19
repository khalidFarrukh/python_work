import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name, " ", host_ip)
port = 1025
s.connect((host_ip, port))
msg = ""
while True:
    temp = s.recv(8)
    if len(temp) == 0:
        break
    msg += temp.decode("utf-8")
print(msg)
s.close()
