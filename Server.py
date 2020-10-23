##################################################################
# Working with the crude sockets
#-----------------------------------------------------------------
# 1. Create socket for TCP/IP streaming server
# 2. Assign address
# 3. Listen to the connections
# 4. Accept connections
# 5. Process connections and data
# 6. Returning the response
#-----------------------------------------------------------------
# Last Touched By : Amin Matola
# Last Touched    : 10/23/2020
#-----------------------------------------------------------------

import threading
from socket import *

class Server:
    
    """Socket Server for local testing network parameters/entities"""
    
    def __init__( self, port = 3000, backlog = 5, flag = True ):
        self.address        = ""
        self.__port         = port
        self.backlog        = backlog
        self.message        = open(r"path/to/htmlfile.html","r+").read().encode()
        self.mime           = b"Content-Type:text/html\r\n\n"
        self.flag           = flag
        self.__clients      = []
        
        self.start_server()
        
    def start_server( self ):
        """ Main function to start listening on this server"""
        
        print("Starting server on port %d" % self.__port)
        self.__server       = socket( AF_INET, SOCK_STREAM )
        self.__server.bind( (self.address, self.__port) )
        
        # Now listen to the following backlog/amount of pending connections
        self.__server.listen( self.backlog )
        
        while self.flag:
            # Now lets try accept one connection
            try:
                sock, addr        = self.__server.accept()
                data              = sock.recv(2048).decode()
        

                if addr[0] not in self.__clients:
                    self.__clients.append(addr[0])
                    print("Received connection from ", addr)
                    if len(data):
                        print("\n","-"*40, "\nReceived Below Data From Socket Host %s:\n%s\n\t%s"%(addr[0],"-"*40, data))
                else:
                    if self.__clients[-1] == addr[0]:
                        print("\n\t%s"%data)
                    else:
                        print("-"*40, "\n%s\n\t%s"%("-"*40, data))


                    
                threading.Thread( target=self.handle_connection, args = (sock,) ).start()
               
            except Exception as e:
                print("Stopping the server")
                self.stop_server()
            
    def stop_server( self ):
        """Stop this instance by setting the flag to false"""
        self.flag = False

    #----------- Lets define function to handle the upcoming connections one-by-one-----
    def handle_connection( self, client ):
        
        """Handles individual socket client"""
        
        client.sendall( self.mime + self.message )

        client.close()

if __name__ == "__main__":
    Server()
