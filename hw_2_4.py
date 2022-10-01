'''
4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)
'''
from datetime import datetime


def get_number():
    while True:
        try:
            a = int(input('Enter a number: '))
            return abs(a)
        except ValueError:
            print('This is not a number, try again please')


def random_num():
    a = datetime.now().microsecond // 100000 / 10
    print(a)
    min = get_number()
    max = get_number()
    if min > max:
        min, max = max, min
    result = min + a * (max-min)
    print(int(result))


random_num()