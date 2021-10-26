"""
    compname = host name
    appnum = port
    comp = ip address
"""

import socket
import sys
     

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if argv_len < 2 or argv_len > 3:
        print("[INFO] usage: %s <compname> <appnum>".format(sys.argv[0]))
        exit()

    # convert the arguments to binary format comp and appnum
    try:
        comp = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print('[ERROR] invalid host : %s' % sys.argv[1])
        exit()
    
    try:
        app_num = int(sys.argv[2])
    except ValueError:
        print('[ERROR] invalid port : %s' % sys.argv[2])
        exit()

    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect the socket to the specified server
        try:
            s.connect((comp, app_num))
        except TimeoutError:
            print("[ERROR] connect failed")
            exit()
        
        text = ''
        buffer = input("input => ")

        s.sendall(str.encode(buffer))
        while True:
            data = s.recv(1024).decode('utf-8')
            text += data
            if not data:
                break

    print('[SUCCES] Received => ', text)