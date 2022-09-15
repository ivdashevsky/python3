#1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


list = [2, 4, 8, 10, 3, 88, 9, 11]
sum = 0
indexes = [] #считывание нечетных индексов
for i in range(len(list)):
    if (i%2 != 0):
        indexes.append(i)

res = "На нечётных индексах элементы "
for i in range(len(indexes)):
        res += str(list[indexes[i]]) + ' '
        sum += list[indexes[i]]
# for i in range(len(list)):
#     if (i%2 != 0) & (i != indexes[-1]):
#         res = res + str(list[i]) + ', '
#         sum+=list[i]
#     elif (i == indexes[-1]):
#         res = res + 'и ' + str(list[i])
#         sum+=list[i]
print(res)
print(sum)