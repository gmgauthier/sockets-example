import socket
from time import sleep


class EchoClient:
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    def __init__(self, host=HOST, port=PORT):
        self._s = socket.socket()
        self._s.connect((host, port))
        print("Client initialized.")

    def echo(self, message="Hello World!"):
        print("Client will send data: '{}'".format(message))
        self._s.sendall(message.encode())
        data = self._s.recv(4096)
        response = data.decode()
        print("Client received data from server: {}".format(response))
        if message == "!quit":
            print("Client terminating.")
            self.close()
            quit(0)
        return repr(response)

    def close(self):
        self._s.close()
