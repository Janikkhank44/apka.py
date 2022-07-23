W = '\033[97;1m' 
R = '\033[97;1m' 
G = '\033[97;1m' 
Y = '\033[97;1m' 
B = '\033[97;1m'
P = '\033[97;1m'
C = '\033[97;1m'
N = '\x1b[0m'


import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor

def logo():
	print ("""
   
 ───────────────────────────────────────────────────────×
  ───────────────────────────────────────────────────────×
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Mr Wasi Qureshi\x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Version :5\x1b[0m\x1b[1;97m] \033[1;37m 
 ───────────────────────────────────────────────────────×
 """)
def logo2():
	#Yahan apna logo paste krna hw
	print ("""
   ____                       __    _ 
  / __ \__  __________  _____/ /_  (_)
 / / / / / / / ___/ _ \/ ___/ __ \/ / 
/ /_/ / /_/ / /  /  __(__  ) / / / / •Mr Qureshi
\___\_\__,_/_/   \___/____/_/ /_/_/ √Master Mind🥺❤️                                                                            
 ───────────────────────────────────────────────────────×
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Mr Wasi Qureshi\x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Version :6\x1b[0m\x1b[1;97m] \033[1;37m 
 ───────────────────────────────────────────────────────×
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Author   : Mr-Qureshi \x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Github   : www.gitclone//github.com/Mr-Qureshi-xd \x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Facebook : www.facebook./MrQureshi-xd \x1b[0m\x1b[1;97m]
───────────────────────────────────────────────────────× 
 """)

def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('termux-setup-storage')

def helpnote():
	print("%s [=>] FOLLOW ME ON  FB TU KNOW ABOUT UPDATES  :)"%(G))
	#yahan nichy httsp sy hata kr apna github aproval link dalna
	subprocess.check_output(["am", "start", "https://github.com/Mr-Qureshi-xd/run.txt/blob/main/run.txt"])
	#yahan apni facebook id link dalna
	exit(" [=>] FACEBOOK :  https://www.facebook.com/MrQureshi.xd")


def notice():

 

	runtxt("\n\033[0;97m  Free 2009 cloning Tool For Free Aproval Join Group ")
	os.system("xdg-open https://www.facebook.com/groups/447671328737321/permalink/2365540383617063/?app=fbl")
	runtxt("\033[0;97m Key Approval ke Lai Group Jion Krein >> %s%s"%(G,basesplit))
	runtxt("\033[0;97m Key group admin ke post pe coment krein")
	os.system("xdg-open https://www.facebook.com/groups/447671328737321/permalink/2365540383617063/?app=fbl")
	subprocess.check_output(["am", "start", "https://www.facebook.com/groups/447671328737321/permalink/2365540383617063/?app=fbl"])
	


        
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			#yahan pr v apna github link dalna aproval wala
			plr = requests.get('https://github.com/Mr-Qureshi-xd/run.txt/blob/main/run.txt').text
			if basesplit in plr:
				key = basesplit
				stat = ("\033[0;97mPREMIUM")
				FY = '\033[0;97m'
				FG = '\033[0;97m'
				GET = '\r'
			else:
				key = ("\033[0;97m -")
				stat = ("\033[0;97mFREE USER")
				FY = '\033[0;90m'
				FG = '\033[0;90m'
				GET = '\033[0;97m [P] GET PREMIUM'
		except requests.exceptions.ConnectionError:
			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))
			exit()
		os.system("clear")
		#yahan logo lagana apna
		print ("""
   ____                       __    _ 
  / __ \__  __________  _____/ /_  (_)
 / / / / / / / ___/ _ \/ ___/ __ \/ / 
/ /_/ / /_/ / /  /  __(__  ) / / / / •Mr Qureshi
\___\_\__,_/_/   \___/____/_/ /_/_/ √Master Mind🥺❤️                                     
 ───────────────────────────────────────────────────────×
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Mr Wasi Qureshi\x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Version : 6\x1b[0m\x1b[1;97m] \033[1;37m 
 ───────────────────────────────────────────────────────×
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Author   : Mr-Qureshi \x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Github   : www.gitclone//github.com/Mr-Qureshi-xd \x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;41m Facebook : www.facebook./MrQureshi-xd \x1b[0m\x1b[1;97m]
───────────────────────────────────────────────────────× 
    """)
		print("%s [%s•%s] %sTOOL NAME : %s2009 Cloning Tool"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s6"%(G,R,G,B,G))
		print("%s [%s•%s] %sYOUR KEY  : %s%s"%(G,R,G,B,G,key))
		print("%s [%s•%