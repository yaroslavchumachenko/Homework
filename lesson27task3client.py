import socket

def main():
    server_host = '127.0.0.1'
    server_port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected to server {server_host}:{server_port}")

    try:
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024)
            print("Server response:", response.decode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()