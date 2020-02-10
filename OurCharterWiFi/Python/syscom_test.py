import subprocess as sp


print('test subprocess library')

file = 'output.txt'

sp.call(['ls','-l'])
sp.call(['touch',file])
sp.call(['vi',file])

print('test complete')
