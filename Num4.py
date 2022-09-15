#4 Напишите программу, которая будет преобразовывать десятичное число в двоичное


def converter(num = 0):
    res = ''
    while (num > 0):
        res = str(num%2) + res
        num = num // 2
    return res

print(converter(45))