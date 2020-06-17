# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

raw_str = argv[1]
#raw_str = input('Enter network address as 192.168.1.0/24 : ')
# raw_str = '217.113.115.3/28'
addr = raw_str.split('/')[0]
mask = int(raw_str.split('/')[1])

b_addr = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*map(int, addr.split('.')))
b_netaddr = b_addr[0:mask]+'0'*(32-mask)

b_mask = '1'*mask+'0'*(32-mask)


print(f'''Network:
{int(b_netaddr[0:8],2):<8} {int(b_netaddr[8:16],2):<8} \
{int(b_netaddr[16:24],2):<8} {int(b_netaddr[24:32],2):<8}
{b_netaddr[0:8]} {b_netaddr[8:16]} {b_netaddr[16:24]} {b_netaddr[24:32]}

Mask:
/{mask}
{int(b_mask[0:8],2):<8} {int(b_mask[8:16],2):<8} \
{int(b_mask[16:24],2):<8} {int(b_mask[24:32],2):<8}
{b_mask[0:8]} {b_mask[8:16]} {b_mask[16:24]} {b_mask[24:32]}

''')
