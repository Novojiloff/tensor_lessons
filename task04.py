import math

print('Решение квадратного уравнения вида Ax^2 + Bx + C = 0\n')

a = int(input('Введите А: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))

discriminant = b**2 - (4 * a * c)

if discriminant > 0:
    x1 = -b + math.sqrt(discriminant) / (2 * a)
    x2 = -b - math.sqrt(discriminant) / (2 * a)
    print('Дискриминант уравнения больше 0. Поэтому корней два.')
    print(f'x1 = {round(x1, 2)}\nx2 = {round(x2, 2)}')
elif discriminant == 0:
    x1 = - b / (2 * a)
    print('Дискриминант уравнения равен 0. Поэтому корень один.')
    print(f'x = {round(x1, 2)}')
else:
    print('Дискриминант уравнения меньше 0. Поэтому корней нет.')
