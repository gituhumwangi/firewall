import socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.103', 8000))
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {response}")

    client_socket.close()

while True:
    user_input = input("Enter message: ")
    send_message(user_input)
