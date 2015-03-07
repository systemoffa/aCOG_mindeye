"""
Broadcast dummy Pupil stream over TCP
used for debugging and 

from https://gist.github.com/toshikurauchi/2beb05eb589504ce9f1f
"""

import zmq
from ctypes import create_string_buffer
from time import sleep
import random

def test_msg():
    dummy_data = str((random.random(),random.random()))
    test_msg = "Pupil\nconfidence:0.695435635564\nnorm_gaze:"+dummy_data+"\n"+\
    "apparent_pupil_size:41.609413147\nnorm_pupil:(0.76884605884552, 0.35504735310872393)\ntimestamp:1389761135.56\n"
    return test_msg
    
def toggle_record():
    return 'R'
    
def toggle_record_name(dir):
    return 'R ' + dir

def main():
    port = "50020"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    address = create_string_buffer("tcp://*:"+port,512)
    
    try:
        socket.bind(address.value)
    except zmq.ZMQError:
        print "Could not set Socket."

#    for i in range(30):
        # send 30 samples and sleep for half a second
    #    socket.send( test_msg() )
    #    sleep(0.5)
    
    socket.send( toggle_record_name('record tester') )
    sleep(3.0)
    socket.send( toggle_record() )


    context.destroy()


if __name__ == '__main__':
    main()