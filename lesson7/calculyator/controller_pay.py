import modul
import view
import operation
import log

def button_click():
    some_str = view.inp()
    some_str = operation.op(some_str)
    modul.init(some_str[0], some_str[1])
    if some_str[2] == '+':
        result = modul.sum()
    elif some_str[2] == '-':
        result = modul.dif()
    elif some_str[2] == '*':
        result = modul.mult()
    elif some_str[2] == '/':
        result = modul.div()
    else:
        result = ('Такой операции нет !')
    view.view_data(f'Результат = {result}')
    log.write(some_str, result)