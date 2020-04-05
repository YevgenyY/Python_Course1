import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf-8"))
sock.close()

sock_short = socket.create_connection(("127.0.0.1", 10001))
sock_short.sendall("ping one more".encode("utf-8"))
sock_short.close()

