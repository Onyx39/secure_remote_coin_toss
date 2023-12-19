import signal
import socket
import random as rd
import hashlib
from time import sleep
from constants import ALICE_SOCKET, BOB_SOCKET

class Alice () :
        
        def __init__ (self) :
            # can stop the server with Ctl+C in shell
            self.shutdown = 0
            signal.signal(signal.SIGINT, self.shutdown)

            # creating socket and making it reusable
            # self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # # binding socket to host and port
            # self.server_socket.bind(('localhost', ALICE_SOCKET))

            # # waiting queue for requests
            # self.server_socket.listen(10)
            # print("waiting request")






            # initialize connection with bob
            # binding socket to host and port
            # print("ask connection")
            self.bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # print("icic")
            self.bob_socket.connect(('localhost', BOB_SOCKET))
            print("icicicicicic")

            # self.server_socket.accept()

            print("Alice is online\n")

            pari = rd.randint(0, 1)
            print(pari)
            if pari == 0 :
                  pari = b'Tales'
            else : pari = b'Heads'

            self.bob_socket.send(str.encode(str(hashlib.sha256(pari).hexdigest())))
            print(pari)

        




Alice()

