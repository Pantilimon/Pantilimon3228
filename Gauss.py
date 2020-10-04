import numpy as np
from numba import njit


def gauss(A):
    A = list(A)
    a = len(A[0])
    b = len(A)
    for k in range(0, a - 1): #По сути выбираем элементы глав. диагонали(те самый, на котрый буем делить)
        for q in range(k + 1, b): #Выбираем столбец, под элементом глав. диагонали, который мы выбрали выше
            w = A[q][k] / A[k][k]
            for z in range(k, a): #Выбираем строку, начиная с элемента, индекс столбца которого равен индексу элемента на диагонаи
                A[q][z] -= w * A[k][z]
    for l in range(b - 1, -1, - 1):
        for t in range(l - 1, -1, - 1):
            p = A[t][l] / A[l][l]
            A[t][a - 1] -= p * A[l][a - 1]
            A[t][l] = 0
    for k in range(0, b):
        print('x_',k , ' = ', A[k][a - 1]/A[k][k])
    print('Вывести конечную матрицу?')
    print('(Ввидите "Да" или "Нет")')
    a = str(input())
    if a == 'Да' or a == 'да':
        for i in range(0, b):
            print(A[i])
@njit
def gauss_fast(A):
    A = list(A)
    a = len(A[0])
    b = len(A)
    for k in range(0, a - 1): #По сути выбираем элементы глав. диагонали(те самый, на котрый буем делить)
        for q in range(k + 1, b): #Выбираем столбец, под элементом глав. диагонали, который мы выбрали выше
            w = A[q][k] / A[k][k]
            for z in range(k, a): #Выбираем строку, начиная с элемента, индекс столбца которого равен индексу элемента на диагонаи
                A[q][z] -= w * A[k][z]
    for l in range(b - 1, -1, - 1):
        for t in range(l - 1, -1, - 1):
            p = A[t][l] / A[l][l]
            A[t][a - 1] -= p * A[l][a - 1]
            A[t][l] = 0
    for k in range(0, b):
        print('x_',k , ' = ', A[k][a - 1]/A[k][k])
    print('Вывести конечную матрицу?')
    print('(Ввидите "Да" или "Нет")')
    a = str(input())
    if a == 'Да' or a == 'да':
        for i in range(0, b):
            print(A[i])
print('Введите кол-во линейнно независимых уравнений (кол-во строк)')
h = int(input())
u = h + 2
print('Введите матрицу: элементы строк вводятся через пробел, переход к следующей строке - "Enter". Имейте ввиду, что кол-во неизестных("длина строки" - 1) должно быть не больше b (кол-ва уравнений).')
while u - 1 > h:
    U = [list(map(float, input().split())) for i in range(h)]
    u = len(U[0])
    if u > h + 1:
        print('Кол-во переменных < кол-ва уравнений, система не имеет решений в общем случае. Введите матрицу заново.')
#Ввод матрицы окончен
gauss_fast(U)
print()
%timeit gauss(a)
%timeit gauss_jit(a)
