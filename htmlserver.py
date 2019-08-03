#----------------------- Working with the crude sockets ----------------------------
# 1. Create socket for TCP/IP streaming server
# 2. Assign address
# 3. Listen to the connections
# 4. Accept connections
# 5. Process connections and data
# 6. Returning the response

#------------------------ Last Touched By : Amin Matola -----------------------------

import socket as soc
from socket import *
import threading

addr        = ""
port        = 3000
backlog     = 5
htmlmessage = open(r"path/to/htmlfile.html","r+").read()
mime        = "Content-Type:text/html\n\n"

server      = socket(AF_INET, SOCK_STREAM)
server.bind((addr, port))

#----------- Lets define function to handle the upcoming connections one-by-one-----
def handle_connection(source):
    source.sendall(mime)
    source.sendall(message)
    source.close()
    
      

#--------- Now listen to the following backlog/amount of pending connections--------
server.listen(backlog)

#----------------- initialize infinite loop to serve forever -------------------------
while 1:
      # Now lets try accept one connection
      sock,addr   = server.accept()
      print("Received connection from ",addr)
        
      threading.Thread(target=handle_connection,args=(sock))
    


