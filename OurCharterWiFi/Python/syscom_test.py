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
    print(Fore.LIGHTCYAN_EX)
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
    #    ,----.
    #   ( WOW! )                         .-.
    #    `----' _                         \ \
    #          (_)                         \ \
    #              O                       | |
    #                o                     | |
    #                  . /\---/\   _,---._ | |
    #                   /^   ^  \,'       `. ;
    #                  ( O   O   )           ;
    #                   `.=o=__,'            \
    #                     /         _,--.__   \
    #                    /  _ )   ,'   `-. `-. \
    #                   / ,' /  ,'        \ \ \ \
    #                  / /  / ,'          (,_)(,_)
    #                 (,;  (,,)

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
    print('                  /         _,--.__   \\    ╚═════╝╚═╝    ╚═╝  ╚═╝╚═╝       ╚═╝╚═╝')
    print("                 /  _ )   ,'   `-. `-. \\     Charter(networks) Auditing Tool by Edward Ayala")
    print("                / ,' /  ,\'        \ \ \ \ ")
    print("               / /  / ,'          (,_)(,_)")
    print('              (,;  (,,)')

    # print(' ██████╗        █████╗        ████████╗')
    # print('██╔════╝       ██╔══██╗       ╚══██╔══╝')
    # print('██║            ███████║          ██║   ')
    # print('██║            ██╔══██║          ██║   ')
    # print('╚██████╗██╗    ██║  ██║██╗       ██║██╗')
    # print(' ╚═════╝╚═╝    ╚═╝  ╚═╝╚═╝       ╚═╝╚═╝')
    
                                                                                                 
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
        usrInput = input('Killing processes will disconnect you from the Internet, would you like to continue? (y/n) ')
        if usrInput == 'y' or usrInput == 'yes':
            print('Killing processes...')
            sp.run(['airmon-ng','check','kill'], capture_output=True)
            t.sleep(5)
            monitorToggle(interface,0)
        elif usrInput == 'n' or usrInput == 'no':
            print('Attempting to toggle Monitor mode, this may not work without killing the interfering processes.')
            monitorToggle(interface,0)
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
        select = int(input(' Select a file:'))
        print(ls[select])
        return ls[select]
    else:
        return ls[0]
    

def readFile():
    file = findFile()
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))


def start():
    
    getInterface(None) # prints interface information



welcome()       # prints title
# start()         # Start the process/function/procedure tree

# -------SANDBOX--------
# readFile()