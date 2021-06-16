import socket as Socket
import json
import sqlite3

conn = sqlite3.connect('shows.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shop
              (id text, coin TEXT, obj TEXT,  FOREIGN KEY (id) REFERENCES Shows (ID))''')
address = "localhost"
port = 3300
dataPackageSize = 1024


def listenClients(connection, clientAddress):
    while 1:
        try:
            data = connection.recv(dataPackageSize)
        except ConnectionError:
            break
        if not data:
            break
        print("Принято сообщение: ", data.decode('utf-8'))
        data_bytes = data
        data = json.loads(data_bytes.decode('utf-8'))
        # cursor.execute("SELECT COUNT(ID) FROM Shop WHERE id = ? AND obj = '1'", (data["id"],))
        # count = cursor.fetchall()
        # print(count)
        # f(count == [(0, )]):
        cursor.execute("INSERT INTO Shop (id, coin, obj) VALUES (?, ?, ?)", (data["id"], data["coin"], data["obj"]))
        conn.commit()
        # else:
            # print("This user already exist")
            # connection.sendall("no".encode())

    print(f"{clientAddress} has disconnect")


def startServer():
    print("Server started")
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen()

    while True:
        try:
            connection, clientAddress = socket.accept()
        except OSError:
            break
        print(f"{clientAddress} has connected")
        listenClients(connection, clientAddress)
    socket.close()
    print("Server has stopped")


if __name__ == '__main__':
    startServer()