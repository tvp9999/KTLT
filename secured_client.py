import socket
from OpenSSL import SSL


def communicate(client_socket):
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

    context = SSL.Context(SSL.TLSv1_2_METHOD)

    # wrap socket with ssl/tls
    ssl_conn = SSL.Connection(context, client_socket)
    ssl_conn.set_connect_state()
    ssl_conn.do_handshake()

    communicate(ssl_conn)


if __name__ == '__main__':
    main()
