# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.


orig = [1.1, 1.2, 3.1, 10.01]

def result(list):
    new_list = list
    for i in range(len(new_list)):
        a = tuple(str(new_list[i]).split('.'))[1] #взятие дробной части
        new_list[i] = int(a) * (10 ** (-len(a)))
    max_n = max(new_list)
    min_n = min(new_list)
    res = max_n - min_n
    return f'Разница между максимальной и минимальной дробью = {res}'

print(orig)
print(result(orig))