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
host_ip = socket.gethostbyname(socket.gethostname())
port = 1025
local_EP = (host_ip, port)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind(local_EP)
    while True:
        message = "Socket programming in python"
        if message == "exit-99":
            break
        s.listen(10)
        print("waiting for a connection....")
        handler = s.accept()
        if handler != None:
            clnt, c_address = handler
            print(f"connection to {c_address} established")
            clnt.send(message.encode("utf-8"))
            clnt.close()
    s.close()
except NameError:
    s.close()
    print(NameError)
except:
    s.close()
    print("something else went wrong")
else:
    s.close()
    print("nothing went wrong")
