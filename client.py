import socket


def auth(client_socket):    
    authenticated = False

    while not authenticated:    
        username = input("Enter username: ")    
        password = input("Enter password: ")

        client_socket.send(username.encode('utf-8'))    # send the msg include username & passwd to server
        client_socket.send(password.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')    # receive msg either "Authenticated" or "..." from server
        print(response)    

        if response == "Authenticated!":
            authenticated = True
        else:
            print("Invalid username or password. Please try again")

    return authenticated


def communicate(client_socket):    # communicate with server
    while True:
        message = input('Client: ')

        if message.lower() == 'quit':
            client_socket.send(message.encode('utf-8'))
            break
        client_socket.send(message.encode('utf-8'))

        msg = client_socket.recv(1024).decode('utf-8')
        print(f'Server: {msg}')

    client_socket.close()


def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print('Connected successfully!')

    if auth(client_socket):
        communicate(client_socket)


if __name__ == '__main__':
    main()
