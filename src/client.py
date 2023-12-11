import socket
import json

class Client:
    def __init__(self):
        print("Client is starting...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.board = self.connect()

    def connect(self):
        try:
            print("Attempting to connect to the server...")
            self.client.connect(self.addr)
            print("Connected to server, waiting for data...")
            data = self.client.recv(4096*8).decode()
            print("Data received from server:", data)
            return json.loads(data)
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            return None

    def disconnect(self):
        try:
            print("Disconnecting from server...")
            self.client.close()
            print("Disconnected.")
        except Exception as e:
            print(f"Error disconnecting from the server: {e}")

    def send(self, message):
        try:
            print(f"Sending message to the server: {message}")
            if isinstance(message, dict):
                self.client.send(json.dumps(message).encode())
            else:
                self.client.send(message.encode())

            response = self.client.recv(1024).decode()
            print('Received from server:', response)
            return json.loads(response)
        except Exception as e:
            print(f"Error sending/receiving data: {e}")
            return None

if __name__ == "__main__":
    client = Client()
    if client.board is not None:
        client.send({"test": "message"})
        client.disconnect()
