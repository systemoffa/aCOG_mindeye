'''
send dummy udp packets

from: https://gist.github.com/mkassner/c66bce144846358d8f4f
'''
MYPORT = 50005

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

while 1:
    data = 'R:' + repr(time.time()) 
#    data = 'R'
    s.sendto(data, ('<broadcast>', MYPORT))
    print "send %s"%data
    time.sleep(5)