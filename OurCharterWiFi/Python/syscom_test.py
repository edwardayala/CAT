import subprocess as sp
import time as t
import signal
import sys
from os import system
from colorama import Fore,Style

# Variables
ROOT = 'sudo'
interfaceMonitor = 'wlan0mon' # Interface name in Monitor Mode
interfaceManaged = 'wlan0'    # Interface name in Managed Mode

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
    
def checkProcesses():
    checkProcessesProc = sp.run([ROOT,'airmon-ng','check'], capture_output=True, text=True)
    if (checkProcessesProc.stdout.find('F')):
        print(Fore.RED,'Found interfering processes',Fore.BLUE,'\n\n Killing processes will disconnect you from the Internet, would you like to continue? (y/n)',Style.RESET_ALL)
        usrInput = input()
        if usrInput == 'y' or usrInput == 'yes':
            print('Killing processes...')
            sp.run([ROOT,'airmon-ng','check','kill'], capture_output=True)
        elif usrInput == 'n' or usrInput == 'no':
            print('Attempting to toggle Monitor mode, this may not work without killing the interfering processes.')
    else:
        print('No interfering processes - GOOD TO GO')

def checkInterface():
    checkInterfaceProc = sp.run([ROOT,'iwconfig'], capture_output=True, text=True)    # Runs 'sudo iwconfig'
    if (checkInterfaceProc.stdout.find(interfaceMonitor) > 0):                    # if the interface is in Monitor mode, good, if not then toggle settings
        print('Interface is in Monitor mode - GOOD TO GO')
        return True
    else:
        print('Interface is not in Monitor mode - Changing to Monitor Mode...')
        checkProcesses()
        return False
        # monitorToggle(interfaceManaged, 0)

def monitorToggle(interface, mode):     # Runs airmon-ng to start/stop Monitor mode
    # checkProcesses()
    if mode == 0:
        sp.run([ROOT,'airmon-ng','start',interface], capture_output=True)   # Toggle Monitor Mode
    else:
        sp.run([ROOT,'airmon-ng','stop',interface], capture_output=True)    # Toggle Managed Mode
        sp.run([ROOT,'NetworkManager'])     # Restart NetworkMananger to connect to Internet

def findTarget():
    if checkInterface == True:
        regex = '\'(My.)\''
        options = ['-R',regex,'-w','targets','--output-format','csv']
        airmon_capture = sp.run([ROOT,options,interfaceMonitor], capture_output=True, text=True)
        # airmon_capture = sp.run([ROOT,'airodump-ng',interfaceMonitor], capture_output=True, text=True)
        print(airmon_capture.stdout)

welcome()       # prints title 



# # KILL INTERFERING PROCESSES
# print('************KILLING TASKS************')
# sp.run(['airmon-ng', 'check', 'kill'])
# print('************TASKS KILLED************')
# t.sleep(3)

# # SET WIRELESS CARD TO MONITOR MODE
# print('************ENTERING MONITOR MODE************')
# sp.run(['airmon-ng', 'start', 'wlan0'])
# t.sleep(3)

# print('************CHECKING WIRELESS CARD STATUS************')
# sp.run('iwconfig')
# t.sleep(1)
# sp.run('NetworkManager')
# # SCAN FOR NEARBY NETWORKS
# sp.run(['airodump-ng', 'wlan0mon'])
# t.sleep(10)
