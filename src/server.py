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
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                if reply.count("White") == 1:
                    nid = "Black"
                else:
                    nid = "White"

                print("Received: ", reply)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(reply))
        except:
            print("")
            break

    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))