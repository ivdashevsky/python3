#5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def negafib (n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negafib(n+2) - negafib(n+1)

def fib (n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []

def fulfib(n):
    for i in range(-n,0):
        list.append(negafib(i))
    
    list.append(0)
    
    for i in range(1,n+1):
        list.append(fib(i))
    
fulfib(5)

print(list) 