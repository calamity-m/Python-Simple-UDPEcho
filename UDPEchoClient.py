#MyEchoClient.py
# Import socket module
import socket


def UDPClient(port):
    
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # connect to the server on local computer
        message = 'Hello!'
        s.sendto(message, ('127.0.0.1', port))
        
        # receive data from the server
        print s.recv(1024)
        # close the connection
        s.close()
    except:
        print "Connection error occured, closing  socket"
        s.close()

if __name__ == '__main__':
    UDPClient(12559)