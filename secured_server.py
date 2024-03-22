import socket
import ssl

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
            print(f"Error: {e}")
            break
    conn.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is waiting on {host}:{port}")

    try:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr[0]}:{addr[1]}")

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="cert.pem", keyfile="private.key")
        ssl_conn = context.wrap_socket(conn, server_side=True)

        handle_client(ssl_conn)
    except socket.error as e:
        print(f"Socket Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
