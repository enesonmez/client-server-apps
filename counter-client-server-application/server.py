import socket
import sys
from datetime import datetime


PORT = 5193
HOST = '127.0.0.1'
QLEN = 6

visits = 0 # counts client connectons


if __name__ == "__main__":
    port = 0
    protocol_number = ''
    argv = sys.argv
    argv_len = len(argv)

    # Check port argument and assign port number
    if argv_len > 1:
        try:
            port = int(argv[2])
            # test for legal value
            if (port < 0):
                print('[ERROR] bad port number {}'.format(argv[2]))
                exit()
        except ValueError:
            port = PORT
    else:
        port = PORT
    
    # Map TCP transport protocon name to protocol number
    protocol_number = socket.getprotobyname('tcp')
    if (protocol_number == 0):
        print("[ERROR] cannot map 'tcp' to protocol number")
        exit()
    
    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol_number) as s:
        # Bind a local address to the socket
        try:
            s.bind((HOST,PORT))
        except socket.error as msg:
            print('[ERROR] bind failed : %s' % str(msg))
            exit()

        print('[INFO] Server listening...')
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
            
            visits += 1
            now = datetime.now()
            current_time = str(now.strftime("%H:%M:%S"))
            buffer = "[SUCCESS - {}] This server has been contacted {} time.".format(current_time, visits)
            conn.sendall(str.encode(buffer))
            conn.close()
            
            


