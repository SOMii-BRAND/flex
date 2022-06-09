import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from crak import my1st
    print("\n\n")
    time.sleep(1)
    my1st()
elif bit == '32bit':
    from crak import my1st
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    my1st()
