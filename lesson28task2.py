import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        
        if not data:
            break
        client_socket.send(data)
    
    client_socket.close()
    print(f"Connection from {address} closed.")


def main():

    host = '127.0.0.1'
    port = 65432
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, address = server_socket.accept()
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
            
    except KeyboardInterrupt:
        print("Server shutting down...")
        server_socket.close()

if __name__ == "__main__":
    main()