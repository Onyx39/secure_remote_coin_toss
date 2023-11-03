import signal
import socket
from time import sleep
from constants import ALICE_SOCKET, BOB_SOCKET

class Bob () :
        
        def __init__ (self) :
            # can stop the server with Ctl+C in shell
            self.shutdown = 0
            signal.signal(signal.SIGINT, self.shutdown)

            # creating socket and making it reusable
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # binding socket to host and port
            # print("ligne 18")
            self.server_socket.bind(('localhost', BOB_SOCKET))
            # (print("ligne 20"))
            # waiting queue for requests
            self.server_socket.listen(10)
            print("waiting request")

            self.server_socket.accept()
            print("connection accepted")
            print("ask connection")

            # initialize connection with bob
            # binding socket to host and port
            # self.alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.alice_socket.connect(('localhost', ALICE_SOCKET))

            # waiting queue for requests
            # self.server_socket.listen(10)


            print("Bob is online\n")
            sleep(2)

            msg = self.server_socket.recv(4096)
            print(msg)
            msg = self.server_socket.recv(4096)
            print(msg)
            msg = self.server_socket.recv(4096)
            print(msg)

Bob()