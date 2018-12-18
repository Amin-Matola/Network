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
message     = "<h1>Hello there, how are you?</h1>"
mime        = "Content-Type:text/html\n\n"

server      = socket(AF_INET, SOCK_STREAM)
server.bind((addr, port))

# Lets define function to handle the upcoming connections one-one

def handle_connection(source):
    source.sendall(mime)
    source.sendall(message)
    source.close()
    
      

# Now listen to the following backlog/amount of pending connections

server.listen(backlog)

# initiate infinite loop to serve forever

while 1:
      # Now lets try accept one connection
      sock,addr   = server.accept()
      threading.Thread(target=handle_connection,args=(sock))
    


