import socket
import mouse
import pickle
def get_mouse_position():
    rhip = open("D:\server_client\_r_server_hip.txt","r").read() # direct internet ip
    port = 1026
    remote_s_ep = (rhip, port)
    while True:
        local_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_cc.connect(remote_s_ep)
        temp = local_cc.recv(1024)
        m_pos = pickle.loads(temp)
        mouse.move(m_pos[0], m_pos[1])
        local_cc.close()
if __name__ == "__main__":
    get_mouse_position()