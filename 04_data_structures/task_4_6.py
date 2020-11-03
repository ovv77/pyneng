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

names = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
str1, str2, str3, str4, str5 = names

print(f'''
{str1:30} {lst[0]}
{str2:30} {lst[1]}
{str3:30} {lst[2]}
{str4:30} {lst[3]}
{str5:30} {lst[4]}
''')






