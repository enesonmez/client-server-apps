import socket
import sys


PORT = 5193
HOST_NAME = "localhost"


if __name__ == "__main__":
    port = 0
    protocol_number = 0
    host = ''
    host_ip_addrs = ''
    argv = sys.argv
    argv_len = len(argv)
    buffer = ''
    
    # Check port argument and assign port number
    if argv_len > 2:
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

    # Check host argument and assign host name
    if argv_len > 1:
        host = argv[1]
    else:
        host = HOST_NAME   
    
    # Convert host name to equivalent IP address
    try:
        host_ip_addrs = socket.gethostbyname(host)
    except socket.gaierror:
        print('[ERROR] invalid host : %s\n' % host)
        exit()
    
    # Map TCP transport protocon name to protocol number
    protocol_number = socket.getprotobyname('tcp')
    if (protocol_number == 0):
        print("[ERROR] cannot map 'tcp' to protocol number\n")
        exit()

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol_number) as s:
        # Connect the socket to the specified server
        try:
            s.connect((host_ip_addrs, port))
        except TimeoutError:
            print("[ERROR] connect failed\n")
            exit()
        
        # Repeatedly read data from socket and write to user's screen
        while (True):
            data = s.recv(1024).decode("utf-8")
            buffer += data
            if not data:
                print(buffer)
                break
        