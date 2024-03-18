import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)


def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return ciphertext, cipher.nonce, tag


def decrypt_message(ciphertext, nonce, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()


# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

connection, client_address = server_socket.accept()
print("Connection from:", client_address)


connection.sendall(key)

while True:
    data = connection.recv(1024)
    if not data:
        break

    ciphertext, nonce, tag = data.split(b'|')
    plaintext = decrypt_message(ciphertext, nonce, tag)
    print("Received message:", plaintext)
    print("Received ciphertext:", ciphertext)

    if plaintext == 'exit':
        print("Closing connection...")
        break

connection.close()