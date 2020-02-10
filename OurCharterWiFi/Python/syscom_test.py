import subprocess as sp
import time as t
import signal
import sys
from os import system
#print('test subprocess library')

#file = 'output.txt'

#sp.call(['ls','-l'])
#sp.call(['touch',file])
#sp.call(['vi',file])

#print('test complete')
print('test aircrack-ng suite')
# KILL INTERFERING PROCESSES
print('KILLING TASKS')
sp.run(['airmon-ng','check','kill'], capture_output=True)
print('TASKS KILLED')
t.sleep(3)
# SET WIRELESS CARD TO MONITOR MODE
print('ENTERING MONITOR MODE')
sp.run(['airmon-ng','start','wlan0'], capture_output=True)
t.sleep(3)
print('CHECKING WIRELESS CARD STATUS')
sp.run('iwconfig')
t.sleep(1)
sp.run('NetworkManager')
# SCAN FOR NEARBY NETWORKS
sys.exit(0)
sp.run(['airodump-ng','wlan0mon'])
t.sleep(10)

