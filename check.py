import os
import requests
import time
import pyfiglet
from colorama import *
import sys

stream = AnsiToWin32(sys.stderr).stream
os.system('cls')
value = pyfiglet.figlet_format('Proxy Checker' , font = 'cosmic')
print(value)
print("")
gf = input("Enter the File Password List [txt] >> ")
file = open(gf)
read = file.readlines()
for i in read :
    try :
        url = "http://www.google.com"
        requests.get(url,proxies={'http':'http://'+i},timeout=(3.05,27))
        print("")
        print(Fore.GREEN + "[+] Proxy Online : " + i, file=stream)
        file = open("OnProxy.txt" , "a")
        file.write(str(i))
        time.sleep(1)
    except requests.ConnectionError :
        print("")
        print(Fore.RED + '[-] Proxy Offline (Connection Error !) : ',i,file=stream)
    except requests.HTTPError :
        print("")
        print(Fore.RED + '[-] Proxy Offline (HTTP Error !) : ',i,file=stream)
        print("")
    except requests.Timeout :
        print("")
        print(Fore.RED + '[-] Proxy Offline (TimeOut Error !) : ',i,file=stream)
    except requests.exceptions.InvalidUR :
        print("")
        print(Fore.RED + '[-] Proxy Offline (URL Is Invalid !)',file.stream)
time.sleep(2)
print("")
print(Fore.WHITE + "-----------------------------",file=stream)
print("")
print(Fore.WHITE + "[+] The Password List is Ended",file=stream)
print("")
print(Fore.WHITE + "-----------------------------",file=stream)
print("")
print(Fore.WHITE + "Plese Press Enter For Exit ...",file=stream)
input("")