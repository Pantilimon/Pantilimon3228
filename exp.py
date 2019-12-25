"""Задачка по ряду Тейлора"""
import math

ITERATIONS = 50

def my_exp(x_0: float):
    """Вычисление экспоненты при помощи частичного суммирования ряда Тейлора"""
    x_pow: int = 1
    multiplier: float = 1
    partial_sum: float = 1
    for n_0 in range(1, ITERATIONS):
        x_pow *= x_0
        multiplier *= 1 / (n_0)
        partial_sum += x_pow * multiplier
    return partial_sum


a: float = float(input())
print(my_exp(a))
print(math.e**(a))
