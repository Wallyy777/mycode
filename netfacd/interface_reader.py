#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n*************Details of Interface - ' + i + '**************')
#    print(netifaces.ifaddresses(i))
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i))[netifaces.AF_LINK][0]['addr']) # print MAC
        print('IP: ', end='')
        print(netifaces.ifaddresses(i))[netifaces.AF_INET][0]['addr']) # print IP address
    except:
        print( 'Failed to collect adapter informatio') # error msg


