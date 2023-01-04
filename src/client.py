from ipaddress import NetmaskValueError
import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.board = self.connect()
        self.board = pickle.loads(self.board)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096*8)

    def disconnect(self):
        self.client.close()

    def send(self, message):
        """
        :param data: str
        :return: str
        """
        self.client.send(message.encode())
        data = self.client.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal

n = Network()
n.send("hello")
print(n.board.squares[0][3].piece)