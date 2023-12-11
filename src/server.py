import socket
from _thread import *
import json
from board import Board

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "localhost"

try:
    s.bind((server, port))
except socket.error as e:
    print(f"Socket binding error: {e}")

s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    board = Board()  # Assuming Board() can be converted to a JSON-serializable format
    conn.send(json.dumps(board.to_dict()).encode())  # Sending the board as a JSON string

    while True:
        try:
            data = conn.recv(8192 * 3).decode()

            if not data:
                print("Client disconnected")
                break

            # Process the data received from the client
            process_client_data(data, board)

            # Send updated board back to client
            conn.sendall(json.dumps(board.__dict__).encode())
        except Exception as e:
            print(f"Error handling client data: {e}")
            break

    print("Lost connection")
    conn.close()

def process_client_data(data, board):
    if data == "winner b":
        board.winner = "b"
        print("[GAME] Player b won in game")
    elif data == "winner w":
        board.winner = "w"
        print("[GAME] Player w won in game")
    elif data == "update moves":
        print("Updating board moves")
        # Add logic to update board moves
    # Add additional conditions as needed

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))
