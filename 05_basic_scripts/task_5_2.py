# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
raw_str = input('Enter network address as 192.168.1.0/24: ')
#raw_str = '10.1.1.0/24'
addr = raw_str.split('/')[0]
mask = int(raw_str.split('/')[1])

template_network = ('''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
''')
template_mask = ('''Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
''')

print(template_network.format(*map(int, addr.split('.'))))

b_str_mask = '1' * mask + '0' * (32 - mask)
b_mask = [b_str_mask[0:8], b_str_mask[8:16], b_str_mask[16:24], b_str_mask[24:]]

print(f'''Mask:
{int(b_mask[0], 2):<8} {int(b_mask[1], 2):<8} {int(b_mask[2], 2):<8} {int(b_mask[3], 2):<8}
{b_mask[0]} {b_mask[1]} {b_mask[2]} {b_mask[3]}
''')
