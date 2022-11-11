#  Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции
# # +, -, /, *. Приоритет операций стандартный.

def add(lst):
    return sum(lst)


def diff(lst):
    res = lst[0]
    for i in lst[1:]:
        res -= i
    return res


def mult(lst):
    res = lst[0]
    for i in lst[1:]:
        res *= i
    return res

def delim(lst):
    res = lst[0]
    for i in lst[1:]:
        res /= i
    return res


def app(txt):
   if '(' in txt:
       start = 0
       for i in range(len(txt)):
           if txt[i] == '(':
               start = i
       fin = start + txt[start:].index(')')
       tmp = txt[start+1:fin]
       result = app(tmp)
       return  app(f'{txt[:start]}{result}{txt[fin+1:]}')
   sing = ''
   for s in '+-*/':
       if s in txt:
           sing = s
           break
   if sing == '':
       return int(txt)
   else:
       lst = list(map(app, txt.split(sing)))
       if sing == '*': return mult(lst)
       elif sing == '/': return delim(lst)
       elif sing == '+': return add(lst)
       elif sing == '-': return diff(lst)



print(app('(11+7)*10-10/2+3+1'))
print(eval('11+7*10-10/2+3+1'))
