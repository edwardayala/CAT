import subprocess as sp
import time as t
import signal
import sys
from os import system
from colorama import Fore,Style

# Variables
ROOT = 'sudo'

# Functions
def welcome():
    print(Fore.RED)
    print('          ▀▀▀██████▄▄▄          ')
    print('                 ▀▀▀████▄       ')
    print('          ▄███████▀   ▀███▄     ')
    print('        ▄███████▀       ▀███▄   ')
    print('      ▄████████           ███▄  ')
    print('     ██████████▄           ███▌   ██████╗ ██╗   ██╗██████╗     ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ██╗   ██╗███╗   ███╗    ██╗    ██╗██╗███████╗██╗')
    print('     ▀█████▀ ▀███▄         ▐███  ██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗ ████║    ██║    ██║██║██╔════╝██║')
    print('       ▀█▀     ▀███▄       ▐███  ██║   ██║██║   ██║██████╔╝    ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝██║   ██║██╔████╔██║    ██║ █╗ ██║██║█████╗  ██║')
    print('                 ▀███▄     ███▌  ██║   ██║██║   ██║██╔══██╗    ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║██║╚██╔╝██║    ██║███╗██║██║██╔══╝  ██║')
    print('    ▄██▄           ▀███▄  ▐███   ╚██████╔╝╚██████╔╝██║  ██║    ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║    ╚███╔███╔╝██║██║     ██║')
    print('  ▄██████▄           ▀███▄███     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝')
    print(' █████▀▀████▄▄        ▄█████    ')
    print(' ████▀   ▀▀█████▄▄▄▄█████████▄                                                 A WiFi Auditing Tool By Edward Ayala')
    print('  ▀▀         ▀▀██████▀▀   ▀▀██  ')                                                                                                                      
    print(Style.RESET_ALL)
    
def getInterface(choice):
    command = ['sudo','iwconfig']
    process = sp.run(command, capture_output=True, text=True)
    output = process.stdout.split(' ')
    for x in output:
        if x == '':
            output.remove(x)
    interface = output[0]
    mode = output[5].split(':')[1]
    if choice == 0:
        return interface
    elif choice == 1:
        return mode
    else:
        print(Fore.BLUE,'Interface:',Fore.YELLOW,interface,Fore.BLUE,'Mode:',Fore.YELLOW,mode,Style.RESET_ALL)
        checkInterface()
    # TODO: Add feature for monitor mode


# More variables
interface = getInterface(0)
mode = getInterface(1)

def checkInterface():
    if interface == 'Monitor':        
        print(Fore.GREEN,'Interface is in Monitor mode!',Fore.BLUE,'\nSearching for target networks...',Style.RESET_ALL)
        findTarget()
    else:
        print(Fore.RED,'Interface is not in Monitor mode',Fore.YELLOW,'\nChanging to Monitor Mode...',Style.RESET_ALL)
        checkProcesses()

def checkProcesses():
    checkProcessesProc = sp.run([ROOT,'airmon-ng','check'], capture_output=True, text=True)
    if (checkProcessesProc.stdout.find('F')):
        print(Fore.RED,'Found interfering processes',Fore.BLUE,'\n\n Killing processes will disconnect you from the Internet, would you like to continue? (y/n)',Style.RESET_ALL)
        usrInput = input()
        if usrInput == 'y' or usrInput == 'yes':
            print('Killing processes...')
            sp.run([ROOT,'airmon-ng','check','kill'], capture_output=True)
            t.sleep(5)
            monitorToggle(interface,0)
        elif usrInput == 'n' or usrInput == 'no':
            print('Attempting to toggle Monitor mode, this may not work without killing the interfering processes.')
            monitorToggle(interface,0)
    else:
        print('No interfering processes - GOOD TO GO')

def monitorToggle(interface, mode):     # Runs airmon-ng to start/stop Monitor mode
    if mode == 0:
        sp.run([ROOT,'airmon-ng','start',interface], capture_output=True)   # Toggle Monitor Mode
        print(Fore.GREEN,'Monitor Mode Enabled!',Style.RESET_ALL)
    else:
        sp.run([ROOT,'airmon-ng','stop',interface], capture_output=True)    # Toggle Managed Mode
        sp.run([ROOT,'NetworkManager'])     # Restart NetworkMananger to connect to Internet
        print(Fore.GREEN,'Monitor Mode Disabled & Internet Capabilities Re-Enabled',Style.RESET_ALL)

def findTarget():
    # airodump_proc = sp.Popen([ROOT,'timeout','12','airodump-ng','-R','\'(TCC.)\'','-w','targets','--output-format','csv',interfaceMonitor], stdout=sp.PIPE)
    airodump_proc = sp.Popen([ROOT,'airodump-ng','-R','\'(My.)\'','-w','targets','--output-format','csv',interface,'&'], stdout=sp.PIPE)
    airodump_capture = airodump_proc.stdout.read().decode('utf-8')
    print(airodump_capture)
    t.sleep(12)
    airodump_proc.send_signal(signal.SIGINT)

welcome()       # prints title
getInterface(None)  # prints interface information

