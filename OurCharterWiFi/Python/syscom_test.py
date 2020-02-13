import subprocess as sp
import time as t
import signal
import sys
from os import system

# KILL INTERFERING PROCESSES
print('************KILLING TASKS************')
sp.run(['airmon-ng', 'check', 'kill'])
print('************TASKS KILLED************')
t.sleep(3)

# SET WIRELESS CARD TO MONITOR MODE
print('************ENTERING MONITOR MODE************')
sp.run(['airmon-ng', 'start', 'wlan0'])
t.sleep(3)

print('************CHECKING WIRELESS CARD STATUS************')
sp.run('iwconfig')
t.sleep(1)
sp.run('NetworkManager')
# SCAN FOR NEARBY NETWORKS
sp.run(['airodump-ng', 'wlan0mon'])
t.sleep(10)
