from ast import Name
import socket

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
# host_ip = socket.gethostbyname(socket.gethostname())
host_ip = "192.168.0.105"
port = 1025
local_EP = (host_ip, port)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind(local_EP)
    s.listen(10)
    print("waiting for a connection....")
    clnt, c_address = s.accept()
    print(f"connection to {c_address} established")
    print("")
    msg = clnt.recv(1024).decode("utf-8")
    print(msg)
    s.close()
