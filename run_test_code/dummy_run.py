#dummy test
#execfile('main.py')

import os
path = os.path.abspath("../nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py")

#from : http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import os, sys, inspect
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)



print path

#with open(path, 'r') as f:
#    stuff = f.read()

#exec(stuff)
execfile(path)
    #CAN'T IMPORT eye module, because there IS none next to run_dummy!!
    
#os.system("~/Desktop/pupil/pupil_src/capture/main.py")





# use this if you want to include modules from a subfolder
'''
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
'''