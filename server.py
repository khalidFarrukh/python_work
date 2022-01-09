import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1024
s.bind((host, port))
s.listen(5)
while True:
    clt, adr = s.accept()
    print(f"connection to {adr} established")
    clt.send("helleooow bro hahahahah".encode("utf-8"))
    clt.close()
