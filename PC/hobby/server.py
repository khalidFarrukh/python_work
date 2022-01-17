import socket

host = "192.168.0.105"
port = 1025
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    client, caddress = s.accept()
    print(f"connection to {caddress} established")
    message = "Socket programming in python"
    client.send(message.encode("utf-8"))
