import platform
import os
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Dumpp32")._login()
elif 'aarch' in arc:
	__import__("somi").Login()
else:
	exit(f' Unknow device machine {arc}')
