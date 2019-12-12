import math

iterations = 50

def my_exp(x):
    """Вычисление экспоненты при помощи частичного суммирования ряда Тейлора"""
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, iterations):
        x_pow *= x  # 
        multiplier *= 1 / (n) # 
        partial_sum += x_pow * multiplier
    
    return partial_sum


a = float(input())
print(my_exp(a))
print(math.e**(a))
