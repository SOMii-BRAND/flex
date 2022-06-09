import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from crak import expetmysite
    print("\n\n")
    time.sleep(1)
    expetmysite()
elif bit == '32bit':
    from crak import expetmysite
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    expetmysite()
