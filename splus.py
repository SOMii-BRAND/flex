import os, platform,time 
try:

		import os,sys,time,random		from uuid import getnode

		import platform

		import mysql.connector

		import requests

		from termcolor import colored

		from colorama import Fore,Back,Style

		from bs4 import BeautifulSoup as bs

		print('\033[1;32;40mSetup is already installed!\033[1;0m')

		sys.exit()

	except ModuleNotFoundError:

		def installer():

			try:

				print('\033[1;36;40mWait please, \033[1;31;40mInstalling resources...\033[1;0m')

				pt=platform.uname()[0]

				if pt.lower()=='windows':

					os.system('pip install colorama termcolor requests bs4 mysql mysql-connector')

				elif pt.lower()=='linux':

					os.system('pkg install mariadb && apt install mariadb && apt install python && apt install git && pip install colorama termcolor requests bs4 mysql mysql-connector')

				else:

					print('\033[1;31;40mUnsuported operating system detected, please make sure you are using linux or windows platform..\033[1;0m')

					sys.exit()

			except KeyboardInterrupt:

				sys.exit('\033[1;31;40mN[+] Service killed!\033[1;0m')

		installer()
try:
   import requests
except:
   os.system('pip install requests')
   
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
 
