# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
sub_lst = ' '.join(' '.join(ospf_route.split('via')).split(',')).split(']')
lst = ' '.join(' '.join(sub_lst).split('[')).split()


print(lst)



tmp = '''
Prefix:\t\t\t {}
AD/Metric\t\t\t {}
'''
print(tmp.format('111', '222'))

