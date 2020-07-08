# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import os, time

addr_error = True
while addr_error:
    os.system('clear')
    addr = input('Введите IP адрес в формате a.b.c.d: ')
    # addr = '524,168,101,1'
    # addr = '132.12.12.12.1'
    # addr = '524.168.101.1'
    # addr = '124,3.168.101.1'

    addr_lst = []
    try:
        for i in addr.split('.'):
            addr_lst.append(int(i))
        # print(addr_lst)
    except ValueError:
        print('неправильный ip адрес ')
        time.sleep(2)
        continue
    else:
        if len(addr_lst) != 4:
            print('неправильный ip адрес ')
            time.sleep(2)
            continue
        for i in addr_lst:
            if i > 255:
                print('неправильный ip адрес ')
                time.sleep(2)
                addr_check = 'failed'
                break
            else:
                addr_check = 'ok'
    if addr_check != 'ok':
        continue

    if 0 < addr_lst[0] < 224:
        print('unicast')
    elif 223 < addr_lst[0] < 240:
        print('multicast')
    elif addr == '255.255.255.255':
        print('local broadcast')
    elif addr == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
    addr_error = False

