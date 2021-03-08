
#  Определить, является ли введенное число простым.
# def simple(number):
#     if number > 1:
#         for k in range(2, number):
#             if number % k == 0:
#                 print(f'\nВведенное число {number} - не простое')
#                 break
#         else:
#             print(f'\nВведенное число {number} - простое')


# number = int(input('Введите число: '))

# simple(number)

#========================================================================
# Нахождение НОД и НОК.
# import math

# number1 = int(input('Введите 1е число: '))
# number2 = int(input('Введите 2е число: '))

# print(f'НОД {number1} и {number2} = {math.gcd(number1, number2)}')
# print(f'НОК {number1} и {number2} = {abs(number1 * number2) // math.gcd(number1, number2)}')

#========================================================================
# Частота использования цифр в диапазоне чисел.

# def digits_in_freq(begin, end):
#     if begin > end:
#         print('Ошибка: начало не может быть больше конца.')
#         return

#     all_freq = {}

#     for i in range(begin, end + 1):
#         string = str(i)

#         for digit in string:
#             if digit in all_freq:
#                 all_freq[digit] += 1
#             else:
#                 all_freq[digit] = 1
#     for key in sorted(all_freq):
#         print(f'{key} встречается {all_freq[key]} раз(а)')
    

# digits_in_freq(begin = int(input('Начало: ')), end = int(input('Конец: ')))




#========================================================================
#  Частота использования символов в тексте.

# def symbols_in_text(text):
#     all_freq = {}

#     for i in text:
#         if i in all_freq:
#             all_freq[i] += 1
#         else:
#             all_freq[i] = 1
    
#     for key in sorted(all_freq):
#         print(f'{key} встречается {all_freq[key]} раз(а)')

# symbols_in_text(text = input('Введите текст: '))


#========================================================================

 # ** FizzBuzz от 0 до 100, требуется наименьшая длина кода.

#  Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, 
# программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати, 
# то программа должна выводить слово FizzBuzz. Задача может показаться очевидной, 
# но нужно получить наиболее простое и красивое решение.

# def fizzbazz():
#     for num in range(1, 101):
#         if num % 3 == 0:
#             print('Fizz', end = ' ')
#         elif num % 5 == 0:
#             print('Buzz', end = ' ')
#         elif num % 15 == 0:
#             print('FizzBuzz', end = ' ')
#         else:
#             print(num, end = ' ')
# fizzbazz()

#========================================================================
# XOR шифрование, на входе сообщение (строка) и ключ шифрования (строка), на выходе зашифрованное сообщение (строка). 
# XOR расшифровывание, на входе зашифрованное сообщение (строка) и ключ (строка), на выходе исходное сообщение (строка).

 
# def encode(text, step):
#     return text.translate(
#         str.maketrans(secret, secret[step:] + secret[:step]))
 
# def decode(text, step):
#     return text.translate(
#         str.maketrans(secret[step:] + secret[:step], secret))

# text = input('Введите текст: ')
# secret = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
# # secret = input('Введите ключ: ')
# step = 3

# encode = encode(text, step)
# print(encode)

# decode = decode(encode, step)
# print(decode)


import math

# print('Решение квадратного уравнения вида Ax^2 + Bx + C = 0\n')

# a = int(input('Введите А: '))
# b = int(input('Введите B: '))
# c = int(input('Введите C: '))

# discriminant = b**2 - (4 * a * c)

# if discriminant > 0:
#     x1 = -b + math.sqrt(discriminant) / (2 * a)
#     x2 = -b - math.sqrt(discriminant) / (2 * a)
#     print('Дискриминант уравнения больше 0. Поэтому корней два.')
#     print(f'x1 = {round(x1, 2)}\nx2 = {round(x2, 2)}')
# elif discriminant < 0:
#     print('Дискриминант уравнения меньше 0. Поэтому корни комплексные.')
#     x1 = complex(-b + discriminant ** 0.5) / (2 * a)
#     x2 = x1.conjugate()
#     print(f"x1 = {x1:.3f}, \nx2 = {x2:.3f}")
# else:
#     x1 = - b / (2 * a)
#     print('Дискриминант уравнения равен 0. Поэтому корень один.')
#     print(f'x = {round(x1, 2)}')
