# Nelson Dane Summer 2022

# Heartbeat client: sends an UDP packet to a given server every 10 seconds.

# Adjust the constant parameters as needed, or call as:
#     beat.py serverip [udp-port]

import sys
from socket import socket, AF_INET, SOCK_DGRAM
from time import time, ctime, sleep

# Variables
SERVERIP = 'SERVER-IP'    # the IP of the host heart.py host server
HBPORT = 43278            # the UDP port that's open on the host server
BEATWAIT = 10             # number of seconds between heartbeats

# In case I wanted to set the variables from the command line (maybe for docker or something idk)
if len(sys.argv)>1:
    SERVERIP=sys.argv[1]
if len(sys.argv)>2:
    HBPORT=sys.argv[2]

# Heartbeat code
hbsocket = socket(AF_INET, SOCK_DGRAM)
print("PyHeartBeat client sending to IP %s , port %d"%(SERVERIP, HBPORT))
print("\n*** Press Ctrl-C to terminate ***\n")
while 1:
    hbsocket.sendto('Thump!'.encode(), (SERVERIP, HBPORT))
    if __debug__:
        print("Time: %s" % ctime(time()))
    sleep(BEATWAIT)