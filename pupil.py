""" 
 ---------------------------------- (O)<< ----------------------------------------------
 aCOG - Beyond the Mind's Eye
 Copyright (C) 2015  Oliver Hatfield, Sara Fox, Benjamin Sitz, Benjamin Sullivan

 pupil.py

 ---------------------------------- (O)<< ----------------------------------------------
"""


import zmq
from threading import Thread
import Queue    #for thread-safe message sending, to workload and to record.


# RESOURCES
#   http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
#   https://docs.python.org/2/library/multiprocessing.html


# NOTES:
#   I think for now I'm just going to use threading, and only move to multiprocessing if I run into trouble.


# QUESTIONS
#   should I derive Thread/Process? or just make functions that threads would target?


class Listener(Thread):
    def __init__(self):
        super(Listener, self).__init__()
        data_port = "5000"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://127.0.0.1:" + data_port)
        self.socket.setsockopt(zmq.SUBSCRIBE, '')
    
    def run(self):
        self.listen()
    
    def listen(self):
        while True:
            data_msg = self.socket.recv()

            items = data_msg.split("\n") 
            msg_type = items.pop(0)
            data_dict = dict([i.split(':') for i in items[:-1] ])
    
            if msg_type == 'Pupil':
                print "raw msg:\n", data_msg
                try:
                    s = ""
                    for key in data_dict:
                        s += str(key) + " "
    
        #        print "keys are: " + s
                #they are: "norm_pos confidence id timestamp diameter"
        #    print "norm_gaze: ", items['norm_gaze']

                except KeyError:
                    pass
            else:
               # process non gaze position events from plugins here\
                pass





class Remote(Thread):
    def __init__(self):
        super(Remote, self).__init__()
        remote_port = '50020'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:" + remote_port)
    
    def run(self):
        self.notify()
    
    def notify(self):
        while True:
            try:
                print "Please input a command to send."
                cmd = raw_input("cmd? > ")
                print cmd
            except EOFError:
                print
                print "Thank you! Terminating..."
                print
                return
            #relay to pupil remote.
            result = self.socket.send(cmd)
            if result is None:
                print "great!"
            else:
                print "broke"
            try:
                confirm = self.socket.recv()
                print confirm
            except zmq.ZMQError:
                confirm = None
                print "erk"

