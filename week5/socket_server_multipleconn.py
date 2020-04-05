import socket
import threading

def process_request(conn, addr):
    print("connected client: ", addr)
    with conn:
        while True:
            try: 
                data = conn.recv(1024)
            except socket.timeout:
                print("close connection     by timeout")
                break

            if not data:
                break
            print(data.decode("utf-8"))
                    

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        conn.settimeout(5) # None, 0, >= 0
    
        th = threading.Thread(target = process_request, args = (conn, addr))
        th.start()
