import os,sys, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests	
bit = platform.architecture()[0]
if bit == '64bit':
    from somi import Login
    time.sleep(3)
    os.system("xdg-open http://mp3playpro.com/")
    Login()
elif bit == '32bit':
    from f32 import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    Login()
 
 
 
