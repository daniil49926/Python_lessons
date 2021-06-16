import socket as Socket
import json
import sqlite3

conn = sqlite3.connect('shows.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)''')
address = "localhost"
port = 3000
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
        # sendall - принимает массив байт
        if(data["action"] == "register"):
            # connection.sendall(data_bytes)
            cursor.execute("SELECT COUNT(ID) FROM shows WHERE name = ?", (data["name"],))
            count = cursor.fetchall()
            print(count)
            if(count == [(0, )]):
                cursor.execute("INSERT INTO shows (name, password) VALUES (?, ?)", (data["name"], data["password"]))
                conn.commit()
            else:
                print("This user already exist")
                connection.sendall("no".encode())
        elif (data["action"] == "login"):
            cursor.execute("SELECT ID FROM shows WHERE name = ? AND password = ?", (data["name"], data["password"]))
            users = cursor.fetchall()
            print(users)
            if(users != []):
                data1 = ", ".join([str(i) for i in users])
                connection.sendall(data1.encode())
            else:
                print("This user does not exist")
                connection.sendall("login_fail".encode())

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