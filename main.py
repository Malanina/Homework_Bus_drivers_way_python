import function as fn
DRIVERS_DATA = 'driver.txt'
BUSES_DATA = 'bus.txt'
WAY_DATA = 'way.txt'


RUN = True

while RUN:
    MODE = fn.main_menu()
    if MODE == '1':
        fn.print_bus(BUSES_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '2':
        fn.add_bus(BUSES_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '3':
        fn.print_driver(DRIVERS_DATA, BUSES_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '4':
        fn.add_driver(DRIVERS_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '5':
        fn.print_way(WAY_DATA, BUSES_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '6':
        fn.add_way(WAY_DATA)
        print()
        input('Нажмите Enter, чтобы вернуться в меню')
    elif MODE == '7':
        print()
        print('Выход')
        RUN = False
    else:
        print()
        input('Нажмите Enter, чтобы вернуться в меню')