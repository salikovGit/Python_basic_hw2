'''2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список)
чисел от 1 до N. Не используйте функцию math.factorial.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''


def get_numbers():
    while True:
        try:
            a = int(input('Enter a number: '))
            return abs(a)
        except ValueError:
            print('This is not a number, try again please')


def lisf_of_facts():
    n = get_numbers()
    result = [1]
    for i in range(1, n):
        result.append((i+1)*result[i-1])
    print(result)


lisf_of_facts()
