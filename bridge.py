""" 
 ---------------------------------- (O)<< ----------------------------------------------
 aCOG - Beyond the Mind's Eye
 Copyright (C) 2015  Oliver Hatfield, Sara Fox, Benjamin Sitz, Benjamin Sullivan

 bridge.py

 ---------------------------------- (O)<< ----------------------------------------------
"""

import subprocess, os
#import multiprocessing
import threading
from Queue import Queue

import pupil
import record



# RESOURCES
#   threading tutorial: http://pymotw.com/2/threading/index.html#module-threading


# NOTES:
#   I think I'll start out with just threading, and only if I have problems will I go to multiprocessing.



# ---:
#   you know, this might not even be necessary. we might as well just fire up pupil
#   ourselves. we just need to send start/stop signals.
def start_pupil():
    path = os.path.abspath("/pupil-0.4.1/pupil_src/capture/main.py")
    # we just need a path relative to the git repo. a local copy of pupil...
#    return subprocess.call('python ~/Desktop/hide/sen\ 15\ \(+\ winter\)/design/nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py',shell=True)
    return subprocess.call('python ' + path, shell=True)





if __name__ == '__main__':
    
    stuff = Queue()
    stuff.put({'diameter' : 40, 'timestamp' : 2000})
    stuff.put({'diameter' : 50, 'timestamp' : 2001})
    stuff.put({'diameter' : 60, 'timestamp' : 2002})
    stuff.put({'diameter' : 45, 'timestamp' : 2003})
    stuff.put({'diameter' : 50, 'timestamp' : 2004})
    stuff.put({'diameter' : 70, 'timestamp' : 2005})
    
    scribe = record.Recorder('test_output.txt', stuff)
    scribe.setDaemon(False)
    scribe.start()
    
    stuff.put({'diameter' : 30, 'timestamp' : 2006})
    stuff.put({'diameter' : 20, 'timestamp' : 2007})
    stuff.put({'diameter' : 80, 'timestamp' : 2008})
    stuff.put({'diameter' : 75, 'timestamp' : 2009})
    
    scribe.ready()
    
    '''
    ear = pupil.Listener()
    ear.setDaemon(False)
    ear.start()
    
    mouth = pupil.Remote()
    mouth.setDaemon(False)
    mouth.start()
    '''
    
#    ear.daemon = False
#    mouth.daemon = False
    
#    ear.start()
#    mouth.start()