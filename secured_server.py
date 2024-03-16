import socket
from OpenSSL import SSL


def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if msg.lower() == 'quit':
                print('Client disconnected!')
                break
            print(f"Client: {msg}")
            response = input("Server: ")
            conn.send(response.encode('utf-8'))
        except Exception as e:
            print(str(e))
            break
    conn.close()


def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is waiting on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr[0]}:{addr[1]}")

    # Tạo context chỉ định version và cung cấp certificate, key 
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.use_privatekey_file('private.key')
    context.use_certificate_file('cert.pem')

    # Đóng gói ssl với SSL/TLS
    ssl_conn = SSL.Connection(context, conn)
    ssl_conn.set_accept_state()
    ssl_conn.do_handshake()

    handle_client(ssl_conn)

    server_socket.close()


if __name__ == "__main__":
    main()
