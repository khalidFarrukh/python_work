from cgi import print_form
import socket


def main():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name : ", host_name)
    print("Host IP   : ", ip_address)
main()
