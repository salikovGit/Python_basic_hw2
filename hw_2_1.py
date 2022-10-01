'''
1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Учтите, что числа могут быть отрицательными

Пример:

67.82 -> 23
0.56 -> 11
'''


def get_numbers():
    while True:
        try:
            a = float(input('Enter a float number: '))
            return abs(a)
        except ValueError:
            print('This is not float, try again please')


def sum_of_digits():
    num = str(get_numbers())
    result = 0
    for el in num:
        try:
            result += int(el)
        except ValueError:
            continue
    return result


print(sum_of_digits())
