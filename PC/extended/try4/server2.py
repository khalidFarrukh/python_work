import pickle
import socket
import mouse
def send_mouse_position():
    hip = socket.gethostbyname(socket.gethostname()) # direct internet ip
    print(hip)
    port = 1026
    local_s_ep = (hip, port)
    while True:
        local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        local_ss.bind(local_s_ep)
        local_ss.listen(10)
        print("waiting for a connection ....")
        remote_cs, r_cs_address = local_ss.accept()
        print(f"connection to {r_cs_address} established")
        print("")
        m_pos = list(mouse.get_position())  # mouse location
        remote_cs.send(pickle.dumps(m_pos))
        remote_cs.close()
        local_ss.close()
if __name__ == "__main__":
    send_mouse_position()