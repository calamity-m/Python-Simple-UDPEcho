#UDPEchoServer
import socket

def UDPServer(port):
    
    # Create our UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "UDP Socket successfuly created"        
    
    try:
       
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket
        s.bind(('', port))
        print "Socket binded to: %s" %(port)
    
        # Start waiting for connections
        while True:
            data, addr = s.recvfrom(1024)
            print 'Connection received from:', addr
            print 'Echoing Back Message'
            
            rtn = "Echo Message: " + data
            
            s.sendto(rtn, addr)
        
    except:
        s.close()
        
if __name__ == '__main__':
    UDPServer(12559)