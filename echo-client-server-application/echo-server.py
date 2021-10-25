import socket

HOST = '127.0.0.1'
PORT = 65432

print('Server opening...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

print('Server listening...')
s.listen(6)

while True:
    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

    conn.close()