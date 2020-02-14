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
    

def checkInterface():
    checkInterfaceProc = sp.Popen([ROOT,'iwconfig'], stdout=sp.PIPE)    # Runs 'sudo iwconfig'
    iwconfig_output = checkInterfaceProc.stdout.read().decode('utf-8')  # save output to variable | use .decode to convert byte to string
    if (iwconfig_output.find(interfaceMonitor) > 0):                    # if the interface is in Monitor mode, good, if not then toggle settings
        print('Interface is in Monitor mode - GOOD TO GO')
    else:
        print('Interface is not in Monitor mode - Changing to Monitor Mode...')
        monitorToggle(interfaceManaged, 0)

def checkProcesses():
    checkProcessesProc = sp.Popen([ROOT,'airmon-ng','check'], stdout=sp.PIPE)
    checkProc_output = checkProcessesProc.stdout.read().decode('utf-8')
    # TODO: check if airmon-ng check has output 
    if (checkProc_output.find('F')):
        print('Found interfering processes - Killing Processes \n This will disconnect you from the Internet')
        # KILL
    else:
        print('No interfering processes - GOOD TO GO')

def monitorToggle(interface, mode):                                     # Runs airmon-ng to start/stop Monitor mode
    sp.run([ROOT,'airmon-ng','check','kill'])                           # Kills interfering processes
    if mode == 0:
        sp.run([ROOT,'airmon-ng','start',interface])                    # Toggle Monitor Mode
    else:
        sp.run([ROOT,'airmon-ng','stop',interface])                     # Toggle Managed Mode
        sp.run([ROOT,'NetworkManager'])                                 # Restart NetworkMananger to connect to Internet

welcome()

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
