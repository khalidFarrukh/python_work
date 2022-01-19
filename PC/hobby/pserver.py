import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name, " ", host_ip)
port = 1025
s.bind((host_ip, port))
s.listen(5)

while True:
    client, caddress = s.accept()
    print(f"connection to {caddress} established")
    message = "Socket programming in python"
    client.send(message.encode("utf-8"))
    if client.close():
        break
s.close()
