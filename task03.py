print('\nРеализуйте скрипт «Светофор» в бесконечном цикле с возможностью прекращения цикла по кодовому слову, например, «выход».\n' + '=' * 30)

while True:
    light_color = input('Введите цвет: ')

    if str.lower(light_color) == 'зеленый':
        print('\nДвижение разрешено!\n')
    elif str.lower(light_color) == 'желтый':
        print('\nДвижение запрещено, но следует приготовиться...\n')
    elif str.lower(light_color) == 'красный':
        print('\nДвижение запрещено!\n')
    elif str.lower(light_color) == 'выход':
        break    
    else:
        print('\nОшибка ввода\n')
