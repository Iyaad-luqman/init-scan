#!/usr/bin/env python3
import subprocess
import re
import sys
import os

class bcolors:
    pink='\033[95m'
    cyan='\033[36m' 
    ENDC = '\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'

def main():
    print(f'''{bcolors.cyan}
    .__       .__  __                                         
    |__| ____ |__|/  |_            ______ ____ _____    ____  
    |  |/    \|  \   __\  ______  /  ___// ___\\__  \  /    \ 
    |  |   |  \  ||  |   /_____/  \___ \\\  \___ / __ \|   |  \\
    |__|___|  /__||__|           /____  >\___  >____  /___|  /
            \/                        \/     \/     \/     \/ 

                                                {bcolors.green}by init__6{bcolors.ENDC}
            
            ''')
    host = sys.argv[1]
    nmap = subprocess.check_output(('nmap %s --min-rate=9999 | grep open ' % host ), shell=True)
    nmap= str(nmap)
    # nmap = '''
    # 53/tcp  open     domain
    # 80/tcp  open     http
    # 443/tcp open     https
    # '''
    nmap = nmap.replace('\'','')
    nmap = nmap.replace('tcp','')
    nmap = nmap.replace('open','\n')
    nmap = nmap.replace('b','\\n')


    pattern = re.compile(r'(?<=\\n)(.*)(?=\/)', re.IGNORECASE)
    result = re.findall(pattern, nmap)
    final = ",".join(result)
    print('')
    print(f"{bcolors.cyan}Open Ports: {bcolors.pink}",final,f"{bcolors.ENDC}")
    print('\n\n')
    print(f"{bcolors.red}Running service enumeration scans on {bcolors.pink}%s {bcolors.ENDC}" % host)
    print('')
    try:
        file = sys.argv[2]
        os.system('nmap -sV -sC -p' + final + ' ' + host + ' | tee ' + file )
    except:
        os.system('nmap -sV -sC -p' + final + ' ' + host)
    
try:
    if sys.argv[1] == '-h':
        
        print('''
Usage:
    %s $ip $file_to_output
              ''' % sys.argv[0])
    else:
        main()
except KeyboardInterrupt:
    exit()
