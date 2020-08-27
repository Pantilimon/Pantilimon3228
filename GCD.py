# Подсчитывает gcd
def gcd_1(a_1, b_1: int)-> int:
    #Подсчитывает gcd рекурсивным методом
    if b_1 == 0:
        return a_1
    return gcd_1(b_1, a_1 % b_1)
a_0: int = int(input('Введите первое число:' + '\n'))
b_0: int = int(input('Введите второе число:' + '\n'))
print('gcd =', gcd_1(a_0, b_0))
