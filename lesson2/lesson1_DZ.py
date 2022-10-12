import math

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день
# выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
deys = int(input('Введите число от 1 до 7: '))
if deys == 6 or deys == 7:
    print('сегодня выходной!!')
elif deys < 6  and deys >= 1:
    print('Работем!!')
else:
    print('ТЫ с Марса!! на земел 7 дней в недели..')


#
#
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def logic(X, Y, Z):
    return not (X or Y or Z) == (not X and not Y and not Z)


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(logic(x, y, z))

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится)
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input('Введите координату X '))
y = int(input('Введите координату Y '))

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


#
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти
# (x и y).
#

number = int(input('Введите число от 1 до 4: '))

if number == 1:
    print('x > 0 and y > 0')
elif number == 2:
    print('x < 0 and y > 0')
elif number == 3:
    print('x < 0 and y < 0')
else:
    print('x > 0 and y < 0')

#
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Введите коардинаты А:')
A_1 = float(input('X: '))
A_2 = float(input('Y: '))
print("Введите коардинаты B:")
B_1 = float(input('X: '))
B_2 = float(input('Y: '))

print('асстояние между  A и B: ', round(math.sqrt((A_1 - A_2) ** 2 + (B_1 - B_2) ** 2), 2))
