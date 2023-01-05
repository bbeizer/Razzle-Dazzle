import socket
from _thread import *
from board import Board
import pickle

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "localhost"
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
current_id = "White"

def threaded_client(conn):
    global current_id
    board = Board()
    data_string = pickle.dumps(board)
    conn.send(data_string)
    current_id = "Black"
    while True:
        try:
            d = conn.recv(8192 * 3)
            data = d.decode("utf-8")

            if not d:
                print("Goodbye")
                break
            else:
                if data == "winner b":
                    board.winner = "b"
                    print("[GAME] Player b won in game")
                if data == "winner w":
                    board.winner = "w"
                    print("[GAME] Player w won in game")

                if data == "update moves":
                    print("board will")

            sendData = pickle.dumps(board)
            conn.sendall(str.encode(sendData))
        except:
            print("")
            break

    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))