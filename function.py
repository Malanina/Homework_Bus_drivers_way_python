import os
from sys import platform
from operator import itemgetter


def main_menu():
    '''вывод меню в консоль'''
    print('''
    Введите номер действия:
1 - вывод автобусов
2 - добавление автобусов
3 - вывод водителей
4 - добавление водителей
5 - вывод маршрута
6 - добавление маршрута
7 - Выход''')
    print()
    return input('Введите номер действия: ')



def write_file(file_name: str, text):
    '''запись файла'''
    with open(file_name, 'w') as data:
        for line in text:
            print(",".join(line), file=data)


def read_file(file_name: str):
    '''чтение файла'''
    result = []
    with open(file_name, 'r') as data:
        for line in data:
            line = line.replace('\n', '')
            result.append(line.split(','))
    return result


def get_data(reqest: str, data_list: list):
    '''возвращает нужную строку, содержащую запрос'''
    for line in data_list:
        if reqest == itemgetter(0)(line):
            return line
    return ['None', 'None', 'None', 'None']


def id_chackin(old_list:list, our_object: str):
    '''проверка ID на уникальность'''
    while True:
        new_id = str(input(f'{our_object} ID: ').lower())
        for i, line in enumerate(old_list):
            if new_id == itemgetter(0)(line):
                print('Введите другой id')
                input('Нажмите Enterб чтобы чтобы попробовать еще раз')
                break
            if new_id != itemgetter(0)(line) \
                and i == len(old_list) - 1:
                return new_id
            continue



def print_bus(file_name: str):
    '''печать автобусов в консоль'''
    buses_list = read_file(file_name)
    print('|№ |\tавтобус ID |\t модель  |\t гос. номер')
    print('-'*60)
    for num, bus in enumerate(buses_list):
        print(f'|{num+1} |\t     {bus[0]} |\t {bus[2]}|\t{bus[1]}')


def add_bus(file_name_buses: str):
    '''добавление автобуса'''
    buses_list = read_file(file_name_buses)
    new_bus_list = []
    new_bus_id = id_chackin(buses_list, 'автобус')
    new_bus_list.append(new_bus_id)
    new_bus_list.append(str(input('гос. номер: ').lower()))
    new_bus_list.append(str(input('модель: ')))
    buses_list.append(new_bus_list)
    print('Автобус добавлен')
    write_file(file_name_buses, buses_list)


def print_driver(file_name_drivers: str, file_name_buses: str):
    '''печать водителей'''
    drivers_list = read_file(file_name_drivers)
    buses_list = read_file(file_name_buses)
    print('|№ |\tводитель ID |\t Фам. И О |\t модель ТС |\t гос. номер')
    print('-'*60)
    for num, driver in enumerate(drivers_list):
        bus_reqest = driver[1]
        bus_data = get_data(bus_reqest, buses_list)
        print(
            f'|{num+1} |\t    {driver[0]}|\t{driver[2]}'
            f'|\t {bus_data[2]}  |\t {bus_data[1]}')


def add_driver(file_name_drivers: str):
    '''добавление водителей'''
    new_driver_list = []
    drivers_list = read_file(file_name_drivers)
    new_driver_id = id_chackin(drivers_list, 'водитель')
    new_driver_list.append(new_driver_id)
    new_driver_list.append(str(input('автобус ID: ').lower()))
    new_driver_list.append(str(input('ФИО: ')))
    drivers_list.append(new_driver_list)
    print('Водитель добавлен')
    write_file(file_name_drivers, drivers_list)


def print_way(file_name_routes: str, file_name_buses: str):
    '''печать маршрутов'''
    routes_list = read_file(file_name_routes)
    buses_list = read_file(file_name_buses)
    print('|№ |\tмаршрут |\tавтобус |\tгос.номер | маршрут')
    print('-'*70)
    for num, route in enumerate(routes_list):
        bus_reqest = route[1]
        bus_data = get_data(bus_reqest, buses_list)
        print(
            f'|{num+1} |\t{route[0]} |\t{bus_data[2]}|'
            f'\t{bus_data[1]} | {route[2]}')


def add_way(file_name_routes: str):
    '''добавление маршрута'''
    new_route_list = []
    routes_list = read_file(file_name_routes)
    new_route_id = id_chackin(routes_list, 'маршрут')
    new_route_list.append(new_route_id)
    new_route_list.append(str(input('автобус ID: ').lower()))
    new_route_list.append(str(input('маршрут автобуса: ')))
    routes_list.append(new_route_list)
    print('Маршрут добавлен')
    write_file(file_name_routes, routes_list)