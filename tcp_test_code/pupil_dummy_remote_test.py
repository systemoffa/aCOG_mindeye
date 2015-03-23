'''
This is a test server. It will listen for commands and echo them.

from: https://gist.github.com/mkassner/c66bce144846358d8f4f
'''

import zmq
import time

port = "50020"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    try:
        msg = socket.recv(flags=zmq.NOBLOCK)
    except zmq.ZMQError :
        msg = None
    if msg:
        print msg
        socket.send("%s - confirmed"%msg)

    time.sleep(.5)
    print 'wait'

context.close()