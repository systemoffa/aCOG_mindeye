'''
resources
http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
https://github.com/pupil-labs/pupil/wiki/Pupil-capture
https://gist.github.com/mkassner/c66bce144846358d8f4f

'''




"""
ideas:
-   could i modify the remote to start broadcasting as well as recording?
-   key listeners are in pygame, if you want that.  
        it appears that world.py is using GLFW, a OpenGL library for windows and callbacks and all that.  
-   check this for calling a module within another module...
    http://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script
    also
    http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
        :P it looks like this is too complicated... too many other modules and dependencies.
"""

import zmq
#    import select, socket
#    import platform
import threading

'''
import imp

eye = imp.load_source('eye', '/Users/djhakamaster/Desktop/hide/sen 15 (+ winter)/design/pupil/pupil_src/capture/eye.py')
world = imp.load_source('world', '/Users/djhakamaster/Desktop/hide/sen 15 (+ winter)/design/pupil/pupil_src/capture/world.py')
main = imp.load_source('main', '/Users/djhakamaster/Desktop/hide/sen 15 (+ winter)/design/pupil/pupil_src/capture/main.py')
main.main()
'''


def data_listen(sock):
    while True:
        
        #set up listener/server first
        
        data_msg = sock.recv()
        print "raw msg:\n", data_msg
        
        items = data_msg.split("\n") 
        msg_type = items.pop(0)
        data_dict = dict([i.split(':') for i in items[:-1] ])
    
        if msg_type == 'Pupil':
            try:
                s = ""
                for key in data_dict:
                    s += str(key) + " "
    
                print "keys are: " + s
                #they are: "norm_pos confidence id timestamp diameter"
            
        #    print "norm_gaze: ", items['norm_gaze']

            except KeyError:
                pass
        else:
           # process non gaze position events from plugins here
            print "msg wasn't from pupil"
            pass


def remote(sock):
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
        result = sock.send(cmd)
        if result is None:
            print "great!"
        else:
            print "broke"
        try:
            confirm = sock.recv()
            print confirm
        except zmq.ZMQError:
            confirm = None
            print "erk"


#server setup
data_port = "5000"
data_context = zmq.Context()
data_sock = data_context.socket(zmq.SUB)
data_sock.connect("tcp://127.0.0.1:" + data_port)
data_sock.setsockopt(zmq.SUBSCRIBE, '')

#remote setup
remote_port = '50020'
remote_context = zmq.Context()  #maybe only allowed one?
remote_sock = remote_context.socket(zmq.REQ)
remote_sock.connect("tcp://localhost:" + remote_port)



        
        
server_t = threading.Thread(target=data_listen, name='tap', args=(data_sock,))
    #farther down in S/O, I guess you just put nothing after the comma.
server_t.daemon = False      #not sure what this is for, but worth a shot
    #i think (if True) it makes this thread end when the main thread ends.
        #which is NOT what i want.
server_t.start()
remote_t = threading.Thread(target=remote, name='remote', args=(remote_sock,))
remote_t.daemon = False
remote_t.start()
        
        
    
    
    










''' SERVER
#network setup
port = "5000"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:"+port)
#filter by messages by stating string 'STRING'. '' receives all messages
socket.setsockopt(zmq.SUBSCRIBE, '')
'''

'''SERVER PIECES'''
'''
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
'''        
        
        
        
        

'''
from: https://gist.github.com/mkassner/c66bce144846358d8f4f
'''

#UDP socket setup

'''
port = 50005  # where do you expect to get a msg?
bufferSize = 1024 # whatever you need

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if platform.system() == 'Darwin':
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
else:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', port))
s.setblocking(0)



#zmq setup
import zmq
context = zmq.Context()
z = context.socket(zmq.REQ)
z.connect("tcp://localhost:50020") #configure for localhost on port 50020
'''
'''REMOTE PIECES'''
'''
while True:
  
    result = select.select([s],[],[])
    #get udp message string
    msg = result[0][0].recv(bufferSize)
    print "message is " + msg
    #relay to pupil remote.
    z.send(msg)
    #await confirmation
    print z.recv()
'''
