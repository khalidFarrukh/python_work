import pickle
import socket
import win32api

def send_mouse_event():
    hip = "192.168.0.105" # direct internet ip
    port = 1027
    local_s_ep = (hip, port)
    while True:
        left_click_event = win32api.GetKeyState(0x01)
        right_click_event = win32api.GetKeyState(0x02)
        middle_click_event = win32api.GetKeyState(0x04)
        if left_click_event<0:
            data = "l"
            local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            local_ss.bind(local_s_ep)
            local_ss.listen(10)
            print("waiting for a connection ....")
            remote_cs, r_cs_address = local_ss.accept()
            print(f"connection to {r_cs_address} established")
            print("")
            remote_cs.send(pickle.dumps(data))
            remote_cs.close()
            local_ss.close()
        elif right_click_event<0:
            data = "r"
            local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            local_ss.bind(local_s_ep)
            local_ss.listen(10)
            print("waiting for a connection ....")
            remote_cs, r_cs_address = local_ss.accept()
            print(f"connection to {r_cs_address} established")
            print("")
            remote_cs.send(pickle.dumps(data))
            remote_cs.close()
            local_ss.close()
        elif middle_click_event<0:
            data = "m"
            local_ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            local_ss.bind(local_s_ep)
            local_ss.listen(10)
            print("waiting for a connection ....")
            remote_cs, r_cs_address = local_ss.accept()
            print(f"connection to {r_cs_address} established")
            print("")
            remote_cs.send(pickle.dumps(data))
            remote_cs.close()
            local_ss.close()

if __name__ == "__main__":
    send_mouse_event()