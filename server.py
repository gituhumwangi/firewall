import socket

allowed_messages = ["Hi", "Hey"]
allowed_address = '192.168.1.103'  # Replace with the allowed client IP address

def process_message(message):
    if message in allowed_messages:
        return "accepted"
    else:
        return "rejected"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.103', 8000))
    server_socket.listen(1)

    print("Listening on 192.168.1.103:8000")

    while True:
        conn, addr = server_socket.accept()

        if addr[0] == allowed_address:
            print(f"Accepted connection from {addr}")
            message = conn.recv(1024).decode('utf-8')
            print(f"Received: {message}")

            response = process_message(message)
            conn.send(response.encode('utf-8'))
        else:
            print(f"Rejected connection from {addr}")

        conn.close()

start_server()
