#2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

orig = [1, 5, 7, 3, 4, 9, 0]


def result (list):
    new_list = []
    len_list = len(list)
    for i in range(len_list // 2 ):
        new_num = list[i] * list[len_list - i - 1]
        new_list.append(new_num)
    if ((len_list / 2) % 2 != 0):
        mid = list[len_list // 2] ** 2
        new_list.append(mid)
        return new_list
    else:
        return new_list


print(result(orig))

