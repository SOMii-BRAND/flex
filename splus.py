import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from zxx import option2
    print("\n\n")
    time.sleep(1)
    option2()
elif bit == '32bit':
    from sp import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
 
