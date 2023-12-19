import signal
import socket
from time import sleep
import hashlib
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

            self.server_socket = self.server_socket.accept()[0]
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

            msg = self.server_socket.recv(4096)[2:-1]
            print(msg)

            tales = hashlib.sha256(b'Tales').hexdigest()
            heads = hashlib.sha256(b'Heads').hexdigest()

            if msg == tales :
                print('You bet Tales')
            else : print('You bet Heads')
                  

Bob()