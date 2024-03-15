import socket


def auth(conn, users):
    authenticated = False

    while not authenticated:
        username = conn.recv(1024).decode('utf-8')
        password = conn.recv(1024).decode('utf-8')

        if username in users and users[username] == password:
            conn.send(b"Authenticated!")
            authenticated = True
        else:
            conn.send(b"Authentication failed!")
    return authenticated


def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if msg.lower() == 'quit':
                print('Client disconnected!')
                break
            print(f"Client: {msg}")
            conn.send(input("Server: ").encode('utf-8'))
        except Exception as e:
            print(str(e))
            break
    conn.close()


def main():
    host = '127.0.0.1'
    port = 12345

    users = {'u1': 'pwd1', 'u2': 'pwd2'}

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server is waiting on {host} : {port}")

    conn, addr = server_socket.accept()

    if auth(conn, users):
        print(f"Connected by  {addr[0]} : {addr[1]}")
        handle_client(conn)

    server_socket.close()


if __name__ == "__main__":
    main()
