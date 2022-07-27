import socket
import mouse
import pickle


def get_mouse_event():
    rhip = open("D:\server_client\_r_server_hip.txt","r").read() # direct internet ip
    port = 1027
    remote_s_ep = (rhip, port)
    while True:
        local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cc.connect(remote_s_ep)
        temp = local_cc.recv(1024)
        if len(temp)>0:
            event = pickle.loads(temp)
            if event == "r":
                mouse.click('right')
                print("                                  right")
            elif event=="l":
                mouse.click('left')
                print("left")
            elif event == "m":
                mouse.click('middle')
                print("             middle")
        local_cc.close()
        # time.sleep(0.1)

if __name__ == "__main__":
    get_mouse_event()
