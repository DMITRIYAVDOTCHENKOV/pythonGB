# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
# N = int(input('Введите число '))
# for i in range(0, N-1):
#     print((-3)**i, end=', ')
# else:
#     print((-3)**(N-1))



# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N1 = int(input('Введите число '))
# arrays = []
# for i in range(1, N1 + 1):
#     arrays.append(f'{i}: ' + str(3 * i + 1))
# print(arrays)




# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')

# arraus2 = str1.split(' ')
# count = 0
# for i , ii in enumerate(arraus2):
#     if arraus2[i] == str2:
#         count +=1
#
# print(count)

arrays3 = str1.count(str2)
len_str2 = len(str2)
i = 0
count = 0
while i < len(str1):
    if str1[i:i + len_str2] == str2:
        count += 1
        i += len_str2
    else:
        i += 1
print(count)
