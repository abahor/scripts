import os
import ctypes
import time

# ctypes.windll.user32.SystemParametersInfoW(20, 0, r"E:\New folder\New folder\UNNamed.png" , 0)

while True:
    for f, d, u in os.walk(r'C:\Users\rolan cemter\Desktop\sd'):
        for i in u:
            if i != 'UNNamed.png':
                if i.split('.')[-1] == 'jpg' or i.split('.')[-1] == 'png':
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, f + '/' + i, 0)
                    time.sleep(200)
                else:
                    pass
