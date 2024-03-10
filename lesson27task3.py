import socket
import multiprocessing

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    print(f"Client {client_address} disconnected")
    client_socket.close()

def main():
    server_host = '127.0.0.1'
    server_port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address))
            process.start()
            client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()