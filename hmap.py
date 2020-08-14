'''CREATED BY ZEROSEC'''
#!/usr/bin/python3

from socket import *
from termcolor import colored
import optparse
from threading import *



def conScan(host,port):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((host,port))
		print(colored(f'[+] {port}/tcp Open','yellow'))
	except:
		print(colored(f"[!] {port}/tcp Closed",'red'))
	finally:
		sock.close()
	
	
	
def portScan(TGTHOST,TGTPORTS):
	try:
		tgtIP = gethostbyname(TGTHOST)
	except:
		print(colored(f"[!] Unknown Host {TGTHOST}",'red'))
	try:
		tgtName = gethostbyaddr(tgtIP)
		print(colored(f'[+] Scan Results for: {tgtName[0]}','green'))
	except:
		print(colored(f'[+] Scan Results for: {tgtIP}','green'))
	setdefaulttimeout(1)
	for port in TGTPORTS:
		t = Thread(target=conScan, args=(TGTHOST, int(port)))
		t.start()


def main():
	print(colored(''' _     _                   
| |   | |                  
| |__ | |____   ____ ____  
|  __)| |    \ / _  |  _ \ 
| |   | | | | ( ( | | | | |
|_|   |_|_|_|_|\_||_| ||_/ 
                    |_|    ''','magenta'))
	print(colored('Port Scanner By Z34053C v1.0.0\n\n\n','magenta'))
	parser = optparse.OptionParser(colored('Usage of program : '+'-H <target host> -p <target port>','blue'))
	parser.add_option('-H', dest='TGTHOST', type='string', help='specify the target host')
	parser.add_option('-p', dest='PGTPORT', type='string', help='specify the target ports separated by comma')
	(options, args) = parser.parse_args()
	TGTHOST = options.TGTHOST
	PGTPORTS = str(options.PGTPORT).split(",")
	if(TGTHOST == None) | (PGTPORTS[0] == None):
		print(parser.usage)
		exit(0)
	portScan(TGTHOST,PGTPORTS)


if __name__ == "__main__":
	main()
