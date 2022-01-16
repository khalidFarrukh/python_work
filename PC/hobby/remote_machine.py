from cgi import print_form
import socket


def main():
    host_name = "www.youtube.com"
    try:
        print(
            "IP address of "
            + host_name
            + " is ( "
            + socket.gethostbyname(host_name)
            + " )"
        )
    except socket.error as e:
        print("Error : {} ".format(e))

if __name__=="__main__":
    main()
