import socket
name = socket.gethostname()
print(name)
ip = socket.gethostbyname(name)
print(ip)