#reads the data from the pupil capture server stream! from here: https://github.com/pupil-labs/pupil/wiki/Pupil-capture

import zmq

#network setup
port = "5000"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:"+port)
#filter by messages by stating string 'STRING'. '' receives all messages
socket.setsockopt(zmq.SUBSCRIBE, '')

while True:
    msg = socket.recv()
    print "raw msg:\n", msg

    items = msg.split("\n") 
    msg_type = items.pop(0)
    items = dict([i.split(':') for i in items[:-1] ])

    if msg_type == 'Pupil':
        try:
            print "norm_gaze: ", items['norm_gaze']

        except KeyError:
            pass
    else:
        # process non gaze position events from plugins here
        pass