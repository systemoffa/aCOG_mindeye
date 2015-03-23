""" 
 ---------------------------------- (O)<< ----------------------------------------------
 aCOG - Beyond the Mind's Eye
 Copyright (C) 2015  Oliver Hatfield, Sara Fox, Benjamin Sitz, Benjamin Sullivan

 bridge.py

 ---------------------------------- (O)<< ----------------------------------------------
"""

import subprocess, os
import multiprocessing
import pupil


# RESOURCES
#   

# NOTE:
#   you know, this might not even be necessary. we might as well just fire up pupil
#   ourselves. we just need to send start/stop signals.
def start_pupil():
    path = os.path.abspath("/pupil-0.4.1/pupil_src/capture/main.py")
    # we just need a path relative to the git repo. a local copy of pupil...
#    return subprocess.call('python ~/Desktop/hide/sen\ 15\ \(+\ winter\)/design/nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py',shell=True)
    return subprocess.call('python ' + path, shell=True)


if __name__ == '__main__':
    
    ear = pupil.Listener()
    ear.daemon = False
    ear.start()
    
    mouth = pupil.Remote()
    mouth.daemon = False
    mouth.start()
    
    
#    ear.daemon = False
#    mouth.daemon = False
    
#    ear.start()
#    mouth.start()