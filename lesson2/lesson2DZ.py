# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественно число ')
sum = 0
for i in number:
    if i != '.' and i != ',' and i != ' ':
        sum += int(i)
print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input('Введите  число '))
composition = 1
for i in range(number):
    i += 1
    composition = i * composition
print(i, composition, end=' ')

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number2 = int(input())
my_list = []
for i in range(1, number2 + 1):
    my_list.append((1 + 1 / i) ** number2)
print(sum(my_list))

# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input())
some_list = []
for _ in range(n):
    some_list.append(random.randint(-n, n))
print(some_list)
with open('filelesson2.txt', 'w', encoding='utf-8') as f:
    for _ in range(n):
        f.write(str(random.randint(0, n - 1)) + '\n')
fact = 1
with open('filelesson2.txt', 'r', encoding='utf-8') as f:
    f = f.read().splitlines()
    for i in f:
        fact *= some_list[int(i)]
print(fact)

# Реализуйте алгоритм перемешивания списка.
some_list = [1, 3, 5, 10]
random.shuffle(some_list)
print(some_list)

some_list = [1, 3, 5, 10]
for _ in range(random.randint(1, 10)):
    i1 = random.randint(0, len(some_list) - 1)
    i2 = random.randint(0, len(some_list) - 1)
    some_list[i1], some_list[i2] = some_list[i2], some_list[i1]

import time

random_number = str(time.time()).split('.')[1]
some_list = [1, 4, 9, 10]
for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
    i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
time.sleep(0.00001)
i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
print(some_list)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)
