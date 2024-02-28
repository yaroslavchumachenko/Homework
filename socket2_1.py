import socket
from encription_func import encrypt_text

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
# sock.listen(2)

while True:
    # Wait for a connection
    print('waiting for a connection')
    # connection, client_address = sock.accept()
    try:
        # print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data, addr = sock.recvfrom(1024)
            # data = connection.recv(1024)
            # print('received {!r}'.format(data))
            if data:
                shifr = encrypt_text(data.decode(), 1)
                
                sock.sendto(shifr.encode(), addr)
                # print('sending data back to the client')
                # connection.sendall(data.upper())
            else:
                print('no data from', addr)
                break

    finally:
        # Clean up the connection
        sock.close()
        # connection.close()