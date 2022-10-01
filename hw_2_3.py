'''
3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
Это происходит до тех пор, пока не будет найден палиндром.
Напишите такую программу, которая найдет палиндром введенного пользователем числа.
'''


def get_number():
    while True:
        try:
            a = int(input('Enter a number: '))
            return abs(a)
        except ValueError:
            print('This is not a number, try again please')


def is_palindrome(num, count=1):
    num = str(num)
    print(num)
    if num == num[::-1]:
        print(f'Palindrome was found in {count} tries ')
    else:
        num = int(num) + int(num[::-1])
        count += 1
        is_palindrome(num, count)


is_palindrome(get_number())
