import socket
import ssl


def communicate(client_socket):
    while True:
        try:
            message = input('Client: ')
            if message.lower() == 'quit':
                client_socket.send(message.encode('utf-8'))
                break
            client_socket.send(message.encode('utf-8'))
            msg = client_socket.recv(1024).decode('utf-8')
            print(f'Server: {msg}')
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()


def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Create SSL context
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Wrap socket with SSL
        ssl_conn = context.wrap_socket(client_socket, server_hostname=host)
        ssl_conn.connect((host, port))
        print('Connected successfully!')

        communicate(ssl_conn)
    except socket.error as e:
        print(f"Socket Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()
