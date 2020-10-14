import socket
from multiprocessing import Process
from random import randint
from os import getpid
from time import sleep


class EchoServer:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    def __init__(self, host=HOST, port=PORT):
        self._host = host
        self._port = port
        print("Server Initializing on Host({0}) and Port({1})".format(self._host, self._port))
        sock = socket.socket()
        sock.bind((self._host, self._port))
        sock.listen(1)
        print("Server Listener initialized")
        conn, addr = sock.accept()
        print('Server Connection From Client:', addr)
        while True:
            data = conn.recv(4096).decode()
            print("Server received data from client {0}: {1}".format(str(addr), str(data)))
            if data == "!quit":
                print("Server Terminating")
                conn.sendall(data.encode())
                break
            response = "Received: " + data
            conn.sendall(response.encode())
        conn.close()


if __name__ == '__main__':
    EchoServer()
