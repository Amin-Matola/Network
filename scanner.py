#################################################################################
# 1. Urls And IP Scanning Module 
# -------------------------------------------------------------------------------
#  Last Touched By: Amin Matola                                                 -
#  Last Touched On: 03/08/2019                                                  -
#--------------------------------------------------------------------------------
from socket import (
                    socket,
                    gethostname, 
                    gethostbyname, 
                    getfqdn, 
                    getservbyport, 
                    inet_aton,
                    AF_INET,
                    SOCK_STREAM
                    )
import re, time

#---------------------------------------- Let's start the game ------------------


class Scanner:
    
    """Network programming class, much from old socket API"""
    
    def __init__( self, what = "ip", where = "https://example.com" ):
        self.area       = what
        self.location   = where
        self.ip         = "127.0.0.1"
        self.name       = ""
        self._proto     = re.compile("https?://")
        self.__ports    = self.get_ports()
        self.__client   = socket()

        # Set the name of area to search (IP/URL)
        self.set_area()
    
        
    def get_ports( self ):
        """ Returns the ports/services to scan for """
        
        return    [21,
                   22,
                   23,
                   25,
                   27,
                   50,
                   53,
                   69,
                   70,
                   80,
                   87, 
                   88,
                   109,
                   110,
                   113,
                   143,
                   1080,
                   8080,
                   8088]

    def is_ip( self, ip ):
        """Detect if the given string is a valid ip"""
        try:
            inet_aton(ip)
        except:
            return False
        
        return True
        
    def detect_what( self ):
        """Return what to detect, protocols, services etc"""
        return self.area.lower()
        
    def protocol( self ):
        """ Detect the protocol used, if string passed is an IP address"""
        try:
            return self._proto.search( self.location ).group()
        except:
            return ""


    def set_area( self, to = "url" ):
        """ Set the area to detect, to IP or URL based on given location"""
        if not self.is_ip( self.location ):
            self.area = to

    def get_valid_url( self, url = "" ):
        """Passing http to socket may render errors, so remove protocol"""
        if not len(url):
            url = self.location
        try:
            return url.strip(self.protocol())
        except:
            return url

    def get_url( self, url = ""):
        if not len(url):
            url = self.location
        if not len(url):
            return getfqdn(self.get_machine_ip())
        return url

    def get_ip( self, url = ""):
        """Get the IP address of the given url"""
        url = self.get_url(url)

        if not self.is_ip( url ):
            try:
                return gethostbyname( self.get_valid_url( url ) )
            except Exception as e:
                return False

        else:
            return url

    def get_machine_ip( self ):
        """Get host ip where this file is running"""
        return gethostbyname(gethostname())

    def get_machine_name( self ):
        """Get host name where this file is running"""
        return gethostname()

    def get_domain_name( self, ip = ""):
        url = self.get_ip(ip)

        if self.is_ip(url):
            return getfqdn(url)

    def get_open_ports( self, url = "" ):
        ports, o_ports, ip = self.get_ports(), [], self.get_ip(url)

        sock_obj           = socket(AF_INET, SOCK_STREAM)
        for port in ports:
            flag           = sock_obj.connect_ex( ( ip, port ) )

            if int( flag ) == 0:
                o_ports.append( port )

            time.sleep(0.001)
        
        return o_ports

    def get_running_services( self, url = ""):
        ports, names = self.get_open_ports(url), []

        for port in ports:
            names.append(getservbyport(port))
        return names

    def reconnect(self):
        self.__client = socket()
        self.__client.connect((self.ip, self.__ports))

    def send_data(self, host = "", port = "", data = ""):
        if not len(host):
            self.ip = host
        if port != "":
            self.__ports = port

        try:
                self.__client.connect((self.ip, self.__ports))
        except OSError:
            self.reconnect()
        
        self.__client.send(data.encode())
        while True:
                try:
                    results = self.read_results()
                    if results != b"" or results != "":
                        print(results)
                    else:
                        break
                except:
                    break
                    

    def read_results(self, buffer = 2048):
            return self.__client.recv(buffer).decode()
