# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
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
    exit(1)
else:
    if len(addr_lst) != 4:
        print('неправильный ip адрес ')
        exit(1)
    for i in addr_lst:
        if i > 255:
            print('неправильный ip адрес ')
            exit(1)

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