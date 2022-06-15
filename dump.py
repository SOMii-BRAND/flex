import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dxxx import _login
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _login()
elif bit == '32bit':
    from d32 import main
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    main()
