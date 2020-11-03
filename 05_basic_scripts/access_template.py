#!/usr/bin/env python3.7
from sys import argv

interface = argv[1]
vlan = argv[2]


access_template = ['switchmode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

protocol = input('Enter protocol:')
print(protocol)
