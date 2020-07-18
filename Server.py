#----------------------- Working with the crude sockets ----------------------------
# 1. Create socket for TCP/IP streaming server
# 2. Assign address
# 3. Listen to the connections
# 4. Accept connections
# 5. Process connections and data
# 6. Returning the response

#------------------------ Last Touched By : Amin Matola -----------------------------


from socket import *
import threading

class Server:
    def __init__( self, port = 3000, backlog = 5, flag = True ):
        self.address        = ""
        self.__port         = port
        self.backlog        = backlog
        self.htmlmessage    = open(r"path/to/htmlfile.html","r+").read()
        self.mime           = "Content-Type:text/html\n\n"
        self.flag           = flag
        
        self.init_server()
        
    def start_server( self ):
        self.__server      = socket( AF_INET, SOCK_STREAM )
        self.__server.bind( (addr, port) )
        
        #----- Now listen to the following backlog/amount of pending connections--------
        self.__server.listen( backlog )
        
        while self.flag:
              # Now lets try accept one connection
              sock, addr   = server.accept()
              print("Received connection from ",addr)
                
              threading.Thread( target=handle_connection, args = (sock) )
            
    def stop_server( self ):
        self.flag = False

    #----------- Lets define function to handle the upcoming connections one-by-one-----
    def handle_connection( self, source ):
        source.sendall( mime )
        source.sendall( message )
        source.close()

        
      
    


