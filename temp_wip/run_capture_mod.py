'''
!!!! :O an answer to our problems!! ^_^
from moritz's forum post: https://groups.google.com/forum/#!topic/pupil-discuss/xgQbJEyQ9jg
'''

import threading
import subprocess
import os

class MyThread(threading.Thread):
    def run(self):
        '''Start your thread here'''
    #    return subprocess.call('python ~/Pupil/pupil_code/pupil_src/capture/main.py',shell=True)
        path = os.path.abspath("../nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py")
        #return subprocess.call('python ' + path,shell=True)
        return subprocess.call('python ~/Desktop/hide/sen\ 15\ \(+\ winter\)/design/nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py',shell=True)
            #MUST backslash SPACE, (, ), and that's it

thread = MyThread()
thread.daemon = True    #   set to True if want Pupil to end when this program does...?
thread.start()
#do your other things here:

print 'hi'

#wait for pupil to stop:
thread.join()

print "Done!"

