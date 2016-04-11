import argparse
import socket
import os
import sys

def Logo():
	print ('''
 /$$   /$$                    
| $$  | $$                    
| $$  | $$  /$$$$$$$  /$$$$$$ 
| $$$$$$$$ /$$_____/ /$$__  $$
| $$__  $$|  $$$$$$ | $$  \ $$
| $$  | $$ \____  $$| $$  | $$
| $$  | $$ /$$$$$$$/| $$$$$$$/
|__/  |__/|_______/ | $$____/ 
                    | $$      
                    | $$      
                    |__/ 1.0                
''')

def main():
	Sis()
	Logo()
	Argumentos()
	Conectar()

def Sis():
	if sys.platform != "linux2":
		os.system("cls")
	else:
		os.system("clear")

def Argumentos():
	global args
	print ("\n[+] Heaven Scan Port\n")
	print ("[+] Digite hsp.py --help para checar o manual\n")
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", dest="host", action="store", help="Use -s para definir o site.Ex: hsp.py -s www.google.com")
	parser.add_argument("-p", dest="port", action="store", help="Use -p para escanear uma porta expercifica Ex: -p 80")
	parser.add_argument('-v', dest="version", action='version', version='%(prog)s 1.0 | Skype - gilmarsilva98')
	args = parser.parse_args()

def Conectar():
	if (args.host and args.port):
		print ("Host Alvo: ",args.host)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		c = s.connect_ex((str(args.host),int(args.port)))
		if c == 0:
			print ("\nPort ",args.port," Open:")
		else:
				print ("\nPort ",args.port," Closed:")
	else:
		quit()
		
main()