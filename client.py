import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting to %s' % 879)

try:
    sock.connect(('localhost', 879))
    
    message = 'Hi!'
    message = bytes(message, "utf-8")
    print('sending %s' % str(message)[2:-1])
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('recieved %s' % data)
    
    print('closing socket')
    sock.close()

except socket.error:
    print('socket error occured')
    sys.exit(1) 
