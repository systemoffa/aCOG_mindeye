""" 
 ---------------------------------- (O)<< ----------------------------------------------
 aCOG - Beyond the Mind's Eye
 Copyright (C) 2015  Oliver Hatfield, Sara Fox, Benjamin Sitz, Benjamin Sullivan

 record.py

 ---------------------------------- (O)<< ----------------------------------------------
"""


from threading import Thread
import Queue


# RESOURCES:
#   https://docs.python.org/2/library/queue.html
#   http://pymotw.com/2/threading/index.html#module-threading
#   http://pymotw.com/2/Queue/index.html#module-Queue

# NOTES:
#   this Queue class seems really useful. maybe try using join() and task_done()?


class Recorder(Thread):
    def __init__(self, fn, queue):
        super(Recorder, self).__init__()
        self.filename = fn
        self.pupil_data = queue   # this is a thread-safe Queue, it just holds onto the reference
        self.begin = False
        print 'inited'
        
    def run(self):
        while not self.begin:
        #    print 'waiting'
            pass
        else:
            print 'ready'
            self.tofile()
        #    print 'data has ' + str(self.data.qsize()) + ' items in it'     # use qsize() for approx size of queue
            print "data output"
            return
    
    def ready(self):        # set when all data has been collected
        self.begin = True
        
    def tofile(self):
        with open(self.filename, 'w') as f:
            while not self.pupil_data.empty():
                datum = self.pupil_data.get()
                f.write(str(datum) + '\n')
        
        pass