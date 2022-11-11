# 1.
# Напишите программу, которая принимает на вход
# два числа и проверяет, является ли одно число
# квадратом другого.
# *Примеры: *
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8, 9 -> нет


# a = int(input('Введите число 1: '))
# b = int(input('Введите число 2: '))
#
# if a ** 2 == b:
#     print(f'Ваше число {a} является квадратом число {b}')
# elif b ** 2 == a:
#     print(f'Ваше число {b} является квадратом число {a}')
# else:
#     print('Не являются квадратом')

# if math.pow(a, 2) == b:
#     print(a)
#     print(f'Ваше число {a} является квадратом число {b}')









# 2. Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них.
#  Примеры:
#  - 1, 4, 8, 7, 5 -> 8
#  - 78, 55, 36, 90, 2 -> 90

# some_list = []
# for _ in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
#     if element > maxx:
#         maxx = element
# print(maxx)


#
# list1 = map(int, input('Введите числа через пробел: ').split())
# max_number = max(list1)
# print('Наибольше число: ', max_number )

# print(max(map(int, input('Введите числа через пробел').split())))




# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#
# number = int(input('Введите число '))
# for i in range(-number, number + 1):
#     print(i, end= ' ')
# print(*(range(-number, number + 1)), sep=', ')


#
# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
#

# number = float(input('Введите число '))
# a = int(number * 10) % 10
# if a > 0:
#     print(a)
# else:
#     print('нет остатка')

# number = (input('Введите число '))
# if '.' not in number:
#     print('нет остатка')
# else:
#     a = (float(number) * 10) % 10
#     print(int(a))

# n = input()
# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t + 1])
# else:
#     print('no')



#
# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number = (int(input('Введите число ')))
if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
    print(f'Число {number} кратно 5, 10 или 15')
else:
    print('NO')












# print("hello")
#
# value = None
# a = 123
# b = 1.23
#
# print(a)
# print(b)
# #
# #print(type(a))
# #print(type(b))
# #
#
# s = 'Hello world'
# print(s)
# print(a, b, s)
#
#
# print('{} - {} - {}'.format(a,b,s))
# print(f'{a} - {b} - {s}')
#
# print('{2} - {1} - {0}'.format(a,b,s))
#
#
# #print('Введите a')
# #a = input()
# #print('Введите b')
# #b = input()
#
# #print(a,b)
#
# a = random.randint(2,23)
# print(a);
#
#
# n = 234
# print(n % 10)
# print((n//10) % 10)

# ---------------------------------
# b = random.randint(10, 99)
# print(b)
# firstNumber = b % 10
# secondNumber = b // 10
# if firstNumber > secondNumber:
#     print(firstNumber)
# else:
#     print(secondNumber)
# ----------------------------------------
# from math import sin
#
# def y(x):
#     return sin(x)/x
# print(y(2))


# НАЙТИ РАССТОЯНИЕ МЕЖДУ ТОЧКИ В ПРОСТРАНСТВЕ 2D/3D
# import math
#
# x1 = 5
# x2 = 8
# y1 = 10
# y2 = 15
#
# d = (x2 - x1 ) **2 + (y2 - y1)**2
# sqrt = math.sqrt(d)
# print(sqrt)


# mass1 = [1, 3, 5, 67, 34]
# i = 0
# while i < len(mass1):
#     mass1[i] = -mass1[i]
#     i += 1
# print(mass1)

# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0


# Проверить истинность функции
# def logic (X, Y, Z):
#     return  not(X or Y or Z) == (not X and not Y and not Z)
# for x in range (0,2):
#     for y in range (0, 2):
#         for z in range (0, 2):
#             print(logic(x, y, z))
