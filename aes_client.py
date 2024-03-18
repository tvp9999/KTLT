import socket
from Crypto.Cipher import AES

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))


def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return ciphertext, cipher.nonce, tag


def decrypt_message(ciphertext, nonce, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()


key = client_socket.recv(16)

while True:

    message = input("Enter message: ")
    ciphertext, nonce, tag = encrypt_message(message)
    data = b'|'.join([ciphertext, nonce, tag])
    client_socket.sendall(data)

    if message == 'exit':
        print("Closing connection...")
        break

client_socket.close()