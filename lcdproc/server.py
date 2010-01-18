import sys
import telnetlib
import time
import urllib

from screen import Screen

class Server(object):
    
    def __init__(self, hostname="localhost", port=13666, debug=False):
        """
        Constructor
        """
        self.debug = debug
        self.hostname = hostname
        self.port = port
        self.tn = telnetlib.Telnet(self.hostname, self.port)
        self.server_info = dict()
        self.screens = dict()
                
    def start_session(self):
        """
        Start Session
        """
        response = self.request("hello") 
        bits = response.split(" ")
        self.server_info.update({
            "server_version": bits[2],
            "protocol_version": bits[4],
            "screen_width": int(bits[7]),
            "screen_height": int(bits[9]),
            "cell_width": int(bits[11]),
            "cell_height": int(bits[13])            
        })                
        return response  
                
    def request(self, command_string):
        """
        Request
        """
        self.tn.write(command_string + "\n")
        if self.debug: print "Telnet Request:  %s" % (command_string)
        response = urllib.unquote(self.tn.read_until("\n"))
        if self.debug: print "Telnet Response: %s" % (response[:-1])
        return response


    def add_screen(self, ref):     
        if ref not in self.screens:   
            response = self.request("screen_add %s" % (ref))
            if "success" not in response: return None
            screen = Screen(ref)
            screen.server = self
            screen.clear()
            self.screens[ref] = screen
            return self.screens[ref]