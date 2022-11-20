import datetime

def write(some_str, result):
    with open('cash.txt', 'a', encoding='utf-8') as l:
        l.write(f'{some_str} = {result}, Время хапроса: {datetime.datetime.now()}' + '\n')