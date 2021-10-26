import socket
import sys

HOST = '127.0.0.1'
QLEN = 6

if __name__ == "__main__":
    appnum = 0
    if len(sys.argv) != 2:
        print("[INFO] usage: %s <appnum>" % sys.argv[0])
        exit()
    else:
        try:
            appnum = int(sys.argv[1])
        except ValueError:
            print("[ERROR] port number arange: 1 to 32767")
            exit()
    

    print('Server opening...')
    # Create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("[ERROR] connection failed : ", str(msg))

    # Bind a local address to the socket
    try:
        s.bind((HOST,appnum))
    except socket.error as msg:
        print('[ERROR] bind failed : %s' % str(msg))
        exit()

    print('[INFO] server listening...')
    # Specify size of request queue
    try:
        s.listen(QLEN)
    except socket.error as msg:
        print('[ERROR] listen failed : %s' % str(msg))
        exit()

    # Main server loop - accept and handle requests
    while True:
        try:
            conn, client_addr = s.accept()
            print('[INFO] Connected by {}'.format(client_addr))
        except socket.error as msg:
            print('[ERROR] accept failed : %s' % str(msg))
            exit()

        buffer = ''
        data = bytearray(1024)
        while True:
            len = conn.recv_into(data,  1024)
            buffer += data.decode("utf-8")
            if len > 0:
                break

        conn.sendall(str.encode(buffer))
        conn.close()
