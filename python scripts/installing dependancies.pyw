import subprocess
import time
file = open('requirments.txt','r')
for i in file.readlines():
    try:
        subprocess.call(['pip','install',i])
        time.sleep(10)
    except:
        pass
