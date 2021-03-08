
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
