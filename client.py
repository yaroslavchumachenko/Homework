import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    msg = "Hello, world"
    s.sendall(msg.encode())
    # s.sendall('Hello, world')
    data, _ = s.recvfrom(1024)
    uppercase = data.decode()

print('Received', uppercase)