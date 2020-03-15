#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime



subprocess.call('clear',shell=True)



remoteServer = raw_input("Enter a host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)



time1 = datetime.now()

try:
    for port in range(1,1025):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print "Port() :Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressec Ctrl+C"
    sys.exit()

except socket.error:
    print "Coudn't connect to server"
    sys.exit()

time2= datetime.now()

timetaken=time2 - time 2

Print 'Time taken to complete port scanning :', timetaken
